# CampusConnect frontend

## Run locally

Start the Flask API from the project root in one terminal:

```powershell
python app.py
```

Start the React app in another terminal:

```powershell
cd frontend
npm install
npm run dev
```

The Vite dev and preview servers proxy `/api/*` requests to Flask at `http://127.0.0.1:5000`. Set `VITE_API_PROXY_TARGET` in `frontend/.env` to change the Flask address.

## Supabase setup for public registrations

The website does not ask visitors to sign in or create an Auth account. Register sends an anonymous browser UUID to Flask; the UUID is kept in local storage to prevent duplicate registrations from that browser. Clearing browser data loses the local My events list.

1. Run [`database/guest_registrations.sql`](../database/guest_registrations.sql) in the Supabase SQL Editor. It makes `registrations.user_id` nullable and adds an anonymous visitor ID with a per-event uniqueness index.
2. Run the updated SQL again if you applied an earlier version. It grants the public API key permission to create anonymous registrations and read only event IDs for capacity counts. It does not expose attendee IDs or emails.
3. Restart Flask. No service role key or Auth account is used for visitor registration.

Visitors are not verified. Someone can clear site data or use another browser to register again. The backend enforces event capacity and prevents duplicate registration IDs for the same event.

The supplied event schema does not include date, location, or category columns. Event cards use those values when present and fall back to `created_at` and generic campus copy otherwise.
