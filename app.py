import os
import uuid
from functools import wraps

from dotenv import load_dotenv
from flask import Flask, g, jsonify, request
from postgrest import APIError, ReturnMethod
from supabase import Client, create_client
from supabase.lib.client_options import ClientOptions

load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_PUBLISHABLE_KEY")

app = Flask(__name__)

# Used to validate bearer tokens. Database operations use a request-scoped
# client so the caller's token (and therefore their RLS identity) is forwarded.
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def api_error(message, status):
    return jsonify({"error": message}), status


def authenticated(handler):
    @wraps(handler)
    def wrapped(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        scheme, _, token = auth_header.partition(" ")
        if scheme.lower() != "bearer" or not token.strip():
            return api_error("A valid Bearer access token is required.", 401)

        token = token.strip()
        try:
            response = supabase.auth.get_user(token)
            user = response.user if response else None
        except Exception:
            user = None

        if not user:
            return api_error("Invalid or expired access token.", 401)

        g.user_id = str(user.id)
        # Constructing a client per request avoids changing shared auth state
        # between concurrent Flask requests.
        g.db = create_client(
            SUPABASE_URL,
            SUPABASE_KEY,
            options=ClientOptions(headers={"Authorization": f"Bearer {token}"}),
        )
        return handler(*args, **kwargs)

    return wrapped


def is_unique_violation(error):
    return getattr(error, "code", None) == "23505" or "23505" in str(error)


@app.get("/")
def index():
    return jsonify({"message": "Events API", "endpoints": [
        "GET /api/events",
        "GET /api/events/<id>",
        "POST /api/guest-registrations",
        "POST /api/registrations",
        "GET /api/me/registrations",
        "GET /api/events/<id>/registrations",
    ]})


@app.get("/api/events")
def list_events():
    try:
        result = supabase.table("events").select("*").execute()
        return jsonify(result.data), 200
    except APIError:
        app.logger.exception("Could not load events")
        return api_error("Could not load events.", 500)


@app.get("/api/events/<event_id>")
def get_event(event_id):
    try:
        result = supabase.table("events").select("*").eq("id", event_id).maybe_single().execute()
        if not result.data:
            return api_error("Event not found.", 404)
        return jsonify(result.data), 200
    except APIError:
        app.logger.exception("Could not load event")
        return api_error("Could not load event.", 500)


@app.post("/api/guest-registrations")
def create_guest_registration():
    """Register an anonymous visitor without creating or authenticating an account."""
    body = request.get_json(silent=True)
    if not isinstance(body, dict) or not body.get("event_id") or not body.get("visitor_id"):
        return api_error("JSON body must include event_id and visitor_id.", 400)
    try:
        visitor_id = str(uuid.UUID(str(body["visitor_id"])))
    except (ValueError, TypeError, AttributeError):
        return api_error("visitor_id must be a valid UUID.", 400)
    guest_db = create_client(SUPABASE_URL, SUPABASE_KEY)
    event_id = str(body["event_id"])
    try:
        event_result = (
            guest_db.table("events")
            .select("id,capacity,status")
            .eq("id", event_id)
            .maybe_single()
            .execute()
        )
        event = event_result.data
        if not event:
            return api_error("Event not found.", 404)

        capacity = event.get("capacity")
        if capacity is not None:
            count_result = (
                guest_db.table("registrations")
                .select("event_id", count="exact")
                .eq("event_id", event_id)
                .execute()
            )
            if (count_result.count or 0) >= capacity:
                return api_error("This event is full.", 409)

        result = guest_db.table("registrations").insert({
            "event_id": event_id,
            "guest_id": visitor_id,
        }, returning=ReturnMethod.minimal).execute()
        return jsonify(result.data[0] if result.data else {}), 201
    except APIError as error:
        if is_unique_violation(error):
            return api_error("This browser is already registered for the event.", 409)
        if getattr(error, "code", None) == "42501":
            return api_error(
                "Anonymous registration permissions are missing. Run database/guest_registrations.sql in Supabase.",
                503,
            )
        app.logger.exception("Could not create guest registration")
        return api_error("Could not create registration.", 500)


@app.post("/api/registrations")
@authenticated
def create_registration():
    body = request.get_json(silent=True)
    if not isinstance(body, dict) or not body.get("event_id"):
        return api_error("JSON body must include event_id.", 400)

    event_id = str(body["event_id"])
    try:
        event_result = (
            g.db.table("events")
            .select("id,capacity,status")
            .eq("id", event_id)
            .maybe_single()
            .execute()
        )
        event = event_result.data
        if not event:
            return api_error("Event not found.", 404)
        existing = (
            g.db.table("registrations")
            .select("id")
            .eq("event_id", event_id)
            .eq("user_id", g.user_id)
            .limit(1)
            .execute()
        )
        if existing.data:
            return api_error("You are already registered for this event.", 409)

        capacity = event.get("capacity")
        if capacity is not None:
            count_result = (
                g.db.table("registrations")
                .select("id", count="exact")
                .eq("event_id", event_id)
                .execute()
            )
            if (count_result.count or 0) >= capacity:
                return api_error("This event is full.", 409)

        result = (
            g.db.table("registrations")
            .insert({"event_id": event_id, "user_id": g.user_id})
            .execute()
        )
        return jsonify(result.data[0] if result.data else {}), 201
    except APIError as error:
        if is_unique_violation(error):
            return api_error("You are already registered for this event.", 409)
        app.logger.exception("Could not create registration")
        return api_error("Could not create registration.", 500)


@app.get("/api/me/registrations")
@authenticated
def my_registrations():
    try:
        result = (
            g.db.table("registrations")
            .select("*,events(*)")
            .eq("user_id", g.user_id)
            .execute()
        )
        return jsonify(result.data), 200
    except APIError:
        app.logger.exception("Could not load registrations")
        return api_error("Could not load your registrations.", 500)


@app.get("/api/events/<event_id>/registrations")
@authenticated
def event_registrations(event_id):
    try:
        event_result = (
            g.db.table("events")
            .select("id,organizer_id")
            .eq("id", event_id)
            .maybe_single()
            .execute()
        )
        event = event_result.data
        if not event:
            return api_error("Event not found.", 404)
        if str(event.get("organizer_id")) != g.user_id:
            return api_error("Only the event organizer can view attendees.", 403)

        registrations = (
            g.db.table("registrations")
            .select("id,user_id,event_id,guest_id,created_at")
            .eq("event_id", event_id)
            .execute()
        )
        user_ids = list({row["user_id"] for row in registrations.data if row.get("user_id")})
        users = []
        if user_ids:
            users_result = (
                g.db.table("users")
                .select("id,email")
                .in_("id", user_ids)
                .execute()
            )
            users = users_result.data
        user_by_id = {str(user["id"]): user for user in users}
        attendees = []
        for registration in registrations.data:
            attendee = (
                user_by_id.get(str(registration["user_id"]))
                if registration.get("user_id")
                else {"email": "Guest attendee"}
            )
            attendees.append({
                **registration,
                "user": attendee,
            })
        return jsonify(attendees), 200
    except APIError:
        app.logger.exception("Could not load event attendees")
        return api_error("Could not load event attendees.", 500)


if __name__ == "__main__":
    app.run(debug=True)
