# Ledger Model

Acme Pay uses a double-entry ledger model. Each business event must write balanced debit and credit entries.

## Charge

A successful charge writes:

| Account | Side | Meaning |
| --- | --- | --- |
| `merchant:{merchant_id}:receivable` | Debit | Money owed to the merchant |
| `platform:clearing` | Credit | Funds pending settlement from the provider |

## Refund

A refund writes:

| Account | Side | Meaning |
| --- | --- | --- |
| `platform:clearing` | Debit | Provider clearing balance reduced |
| `merchant:{merchant_id}:receivable` | Credit | Merchant receivable reduced |

## Invariants

- Every write must balance debits and credits.
- Ledger entries should be immutable after insertion.
- Refund totals must not exceed the original payment amount.
- A failed payment must not create ledger entries.

## Known Gap

Partial refunds are only checked against the original amount. A production implementation needs cumulative refund tracking so multiple partial refunds cannot exceed the charge total.

