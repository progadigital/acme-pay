# Threat Model

## Assets

- Merchant balances
- Payment and refund state
- Provider credentials
- Provider webhook payloads
- Audit log history

## Threats

| Threat | Impact | Mitigation |
| --- | --- | --- |
| Duplicate payment request | Customer charged twice | Idempotency key lookup and unique database constraint |
| Replayed provider webhook | Duplicate downstream processing | Webhook inbox keyed by provider event ID |
| Forged provider webhook | Fake payment state transition | Provider signature verification |
| Unauthorized refund | Merchant revenue loss | Admin role checks and audit logs |
| Ledger mutation | Accounting history corrupted | Append-only ledger table and restricted write path |

## Residual Risk

The largest known gap is webhook authenticity. The code demonstrates event deduplication, but a real deployment must verify provider signatures before the inbox records an event as processed.

