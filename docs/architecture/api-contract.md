# API Contract

The demo code does not run a web server, but the product contract is documented so repository-query tools can answer API questions.

| Method | Path | Purpose | Required Role |
| --- | --- | --- | --- |
| `POST` | `/v1/payment_intents` | Create and capture a payment intent | `merchant:write` |
| `POST` | `/v1/refunds` | Refund a succeeded payment intent | `refund:write` |
| `POST` | `/v1/webhooks/provider` | Receive provider webhook events | `provider:webhook` |
| `GET` | `/v1/merchants/{merchant_id}/risk` | Inspect merchant risk status | `risk:read` |
| `GET` | `/v1/audit_events` | Search administrative audit events | `audit:read` |

## Idempotency

Payment creation requires an idempotency key. The API should return the existing payment intent if the same key is retried. This protects customers from duplicate charges during client retries and network timeouts.

## Refund Authorization

Refunds require the `refund:write` role and should emit an audit event with the actor ID, refund ID, payment intent ID, merchant ID, and reason.

## Webhook Authentication

Provider webhooks must be signed. The current demo code models event deduplication, but signature verification is intentionally left as a documented launch gap.

