create table payment_intents (
  id text primary key,
  merchant_id text not null,
  amount_cents integer not null check (amount_cents > 0),
  currency text not null,
  idempotency_key text not null unique,
  payment_method_token_hash text not null,
  provider_charge_id text,
  provider_name text not null default 'sandbox',
  status text not null,
  created_at timestamptz not null default now()
);

create table ledger_entries (
  id bigserial primary key,
  account text not null,
  side text not null check (side in ('debit', 'credit')),
  amount_cents integer not null check (amount_cents > 0),
  currency text not null,
  source_id text not null,
  created_at timestamptz not null default now()
);

create table webhook_events (
  provider_event_id text primary key,
  event_type text not null,
  object_id text not null,
  processed_at timestamptz not null default now()
);

create table admin_audit_log (
  id bigserial primary key,
  actor_id text not null,
  action text not null,
  target_id text not null,
  metadata jsonb not null default '{}',
  created_at timestamptz not null default now()
);

create table merchant_risk_assessments (
  id bigserial primary key,
  merchant_id text not null,
  decision text not null check (decision in ('approve', 'review', 'block')),
  score integer not null check (score >= 0),
  signals jsonb not null default '[]',
  created_at timestamptz not null default now()
);

create table provider_routing_enrollments (
  merchant_id text primary key,
  fallback_enabled boolean not null default false,
  primary_provider text not null,
  fallback_provider text,
  updated_at timestamptz not null default now()
);
