# Runbook: Ledger Reconciliation Failure

Use this runbook when the ledger reconciliation dashboard shows unmatched balances.

## Checks

1. Identify the affected account and source ID.
2. Confirm every source event wrote equal debit and credit totals.
3. Compare provider charge and refund state against Acme Pay payment intent state.
4. Check whether a manual database change bypassed the ledger service.
5. Look for partial refunds that exceed the expected cumulative amount.

## Mitigation

- Pause payout generation for affected merchants.
- Create reversal entries rather than mutating existing ledger entries.
- Attach source IDs, ledger entries, and provider references to the incident record.

## Escalation

Page the ledger owner if platform clearing is off by more than 100 USD or if more than one merchant is affected.

