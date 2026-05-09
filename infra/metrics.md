# Metrics

Acme Pay should emit the following production metrics.

## Payments

- `payment_intent.created.count`
- `payment_intent.succeeded.count`
- `payment_intent.failed.count`
- `payment_provider.timeout.count`
- `payment_provider.decline.count`

## Idempotency

- `payment_intent.idempotency_reuse.count`
- `payment_intent.missing_idempotency_key.count`

## Webhooks

- `webhook.received.count`
- `webhook.duplicate_suppressed.count`
- `webhook.signature_invalid.count`
- `webhook.processing_latency_ms`

## Ledger

- `ledger.entry.created.count`
- `ledger.balance_reconciliation.failed.count`

## Risk

- `risk.assessment.created.count`
- `risk.decision.review.count`
- `risk.decision.block.count`
- `risk.override.created.count`

