# System Overview

Acme Pay is a fictional payments orchestration service for merchant platforms. The service owns payment intent state, provider routing, idempotency, refund coordination, ledger entries, webhook ingestion, and audit logs.

## Primary Components

- API service: accepts merchant-facing payment and refund requests.
- Payment service: validates intent state and calls the configured provider adapter.
- Provider adapter: wraps the external processor contract.
- Ledger: records balanced accounting entries for successful charges and refunds.
- Webhook inbox: deduplicates provider events before downstream processing.
- Risk worker: reviews merchant and transaction signals before payouts.
- Admin audit log: records support and operations changes.

## Request Flow

1. A merchant creates a payment intent with an idempotency key.
2. The payment service checks for an existing intent with the same key.
3. If no intent exists, the service calls the provider adapter.
4. Successful charges create two ledger entries: merchant receivable debit and platform clearing credit.
5. Failed charges are stored as failed intents and do not create ledger entries.
6. Provider webhooks are accepted only once per provider event ID.

## Data Ownership

The payment service owns payment intent state. The ledger owns accounting history and should be append-only. Provider charge IDs are treated as external references, not primary state.

## Important Tradeoff

The demo implementation stores payment intents and webhook inbox state in memory. A production implementation would move those records into durable tables with unique indexes on `idempotency_key` and `provider_event_id`.

