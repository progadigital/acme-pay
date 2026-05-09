# Track cumulative partial refunds

## Background

`PaymentService.refund` checks that a single refund does not exceed the original charge amount, but it does not track cumulative refund totals.

## Acceptance Criteria

- Allow multiple partial refunds.
- Prevent cumulative refunds from exceeding the original amount.
- Preserve the existing ledger balancing invariant.
- Add tests for two valid partial refunds and one excessive partial refund.
- Document the refund behavior in `docs/architecture/ledger-model.md`.

