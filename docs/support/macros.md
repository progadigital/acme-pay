# Support Macros

## Payment Failed

We could not complete the payment because the processor declined the payment method. Ask the customer to use a different method or contact their bank.

Internal note: check `provider_charge_id`, decline code, merchant risk status, and whether the merchant retried with a stable idempotency key.

## Refund Pending

The refund has been created and is waiting for processor settlement. Most refunds appear on the customer's statement within 5 to 10 business days.

Internal note: verify the payment intent is `refunded`, confirm ledger reversal entries exist, and check provider refund state.

## Payout Delayed

We are reviewing the payout status and will update you when the processor confirms settlement timing.

Internal note: follow `docs/runbooks/payout-delay.md` and check for risk holds before promising a payout date.

