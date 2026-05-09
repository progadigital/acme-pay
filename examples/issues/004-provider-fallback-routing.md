# Add explicit provider fallback routing

## Background

Provider fallback routing is intentionally not automatic. The provider outage runbook says to fail closed unless a merchant is enrolled for fallback routing.

## Acceptance Criteria

- Add a routing policy object that evaluates merchant enrollment.
- Record which provider was selected on each payment intent.
- Add tests for primary provider success, primary provider outage, and fallback-disabled merchants.
- Update `docs/architecture/provider-routing.md`.

