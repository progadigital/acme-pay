# Runbook: Payout Delay

Use this runbook when merchants report missing or delayed payouts.

## Checks

1. Confirm the merchant ID and payout date.
2. Check provider status for payout incidents.
3. Compare `platform:clearing` balance against pending payout records.
4. Review recent refund spikes for the merchant.
5. Check whether the merchant is blocked by risk review.

## Mitigation

- If the provider is delayed, update the merchant status page and support macro.
- If ledger balances are inconsistent, pause payout generation for the merchant and escalate to engineering.
- If risk review is blocking payout, route to Trust and Safety with the merchant ID and reason code.

## Escalation

Page payments on-call if ledger balances do not reconcile or if more than 10 merchants are affected.

