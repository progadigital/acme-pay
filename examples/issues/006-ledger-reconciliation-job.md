# Add ledger reconciliation job

## Background

The ledger is append-only, but there is no scheduled reconciliation job comparing provider state, payment intent state, and ledger entries.

## Acceptance Criteria

- Add a reconciliation job that groups entries by source ID.
- Report unbalanced sources.
- Report payment intents that succeeded without ledger entries.
- Report refunds without reversal entries.
- Document alert thresholds in `infra/metrics.md`.

