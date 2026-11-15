-- Allows visitors to register anonymously without a Supabase Auth user.
-- The Flask API writes these rows using a server-only service role key.
alter table public.registrations
  alter column user_id drop not null;

alter table public.registrations
  add column if not exists guest_id uuid;

create index if not exists registrations_event_id_idx
  on public.registrations (event_id);

create unique index if not exists registrations_event_guest_id_uidx
  on public.registrations (event_id, guest_id)
  where guest_id is not null;

-- Restrict the public API key to guest writes and an event_id-only count query.
grant usage on schema public to anon;
revoke all on table public.registrations from anon;
grant insert (event_id, guest_id) on table public.registrations to anon;
grant select (event_id) on table public.registrations to anon;

-- These policies apply when RLS is enabled on registrations. They do not
-- expose attendee emails or visitor IDs through SELECT.
do $$
begin
  if not exists (
    select 1 from pg_policies
    where schemaname = 'public'
      and tablename = 'registrations'
      and policyname = 'anon_guest_registration_insert'
  ) then
    create policy anon_guest_registration_insert
      on public.registrations for insert to anon
      with check (user_id is null and guest_id is not null);
  end if;

  if not exists (
    select 1 from pg_policies
    where schemaname = 'public'
      and tablename = 'registrations'
      and policyname = 'anon_guest_registration_count'
  ) then
    create policy anon_guest_registration_count
      on public.registrations for select to anon
      using (true);
  end if;
end $$;
