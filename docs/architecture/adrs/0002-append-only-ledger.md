# ADR 0002: Use an Append-Only Ledger

Status: Accepted

## Context

Payments, refunds, disputes, and payouts all need a trustworthy accounting trail. Mutable balance rows are easy to query but difficult to audit after bugs or manual corrections.

## Decision

Acme Pay records ledger movements as append-only debit and credit entries. Balance views are derived from entries rather than stored as the source of truth.

## Consequences

- Every business event must write balanced entries.
- Corrections require reversal entries instead of updates.
- On-call engineers can reconcile balances by replaying ledger entries.

