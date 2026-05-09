# ADR 0001: Require Idempotency Keys for Payment Creation

Status: Accepted

## Context

Payment creation can be retried by merchants, browsers, queues, and network clients. Without an idempotency key, retrying a request may create more than one provider charge.

## Decision

Every `POST /v1/payment_intents` request must include an idempotency key. Acme Pay stores one payment intent per key and returns the existing intent when a duplicate request arrives.

## Consequences

- Merchant integrations must generate stable keys per checkout attempt.
- The database must enforce a unique constraint on `payment_intents.idempotency_key`.
- Support can use idempotency keys to debug retry behavior.

