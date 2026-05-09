# Audit Events

Audit events capture privileged actions performed by operators, support agents, and automated jobs.

## Required Fields

- `actor_id`: human or service identity performing the action
- `action`: stable action name
- `target_id`: merchant, payment intent, refund, or provider credential ID
- `metadata`: structured details needed for investigation

## Required Actions

| Action | When |
| --- | --- |
| `refund.created` | Any refund created by an operator or support workflow |
| `risk.override_created` | Any manual risk override |
| `provider_key.rotated` | Provider credential rotation |
| `payout.paused` | Merchant payout pause |

## Gap

The `AuditLog` helper exists in code, but `PaymentService.refund` does not yet require `actor_id` or write `refund.created`. This gap is tracked by `examples/issues/003-add-admin-audit-events-for-refunds.md`.

