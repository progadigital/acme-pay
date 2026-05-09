# Runbook: Merchant Risk Review

Use this runbook when a payment or payout is blocked by risk signals.

## Signals

- `large_payment`: amount is at least 100,000 cents
- `cross_border_payment_method`: payment method country differs from merchant country
- `new_merchant`: merchant account is less than 14 days old

## Decisions

- `approve`: allow the payment or payout
- `review`: queue for Trust and Safety
- `block`: prevent the operation until manual review completes

## Operator Notes

Do not override a block without recording an audit event. If a merchant disputes the decision, attach the risk assessment and relevant ledger entries to the support case.

