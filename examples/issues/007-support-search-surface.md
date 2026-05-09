# Add support search surface

## Background

Support agents need to search by payment intent ID, merchant ID, provider charge ID, and idempotency key.

## Acceptance Criteria

- Add a read-only support search model.
- Mask payment method token data.
- Include refund, ledger, webhook, and audit event summaries.
- Link support copy to `docs/support/macros.md`.

