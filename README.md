# Acme Pay

Acme Pay is a fictional payments product used as a sample repository for exploring Releap.

It is intentionally small, but it is shaped like a real software project. The repository includes payment-domain code, API examples, architecture notes, security docs, runbooks, incident writeups, tests, ownership metadata, and a `.lensignore` example.

Use it to see how Releap can answer questions across source code, documentation, operational context, and product decisions.

## What Acme Pay Models

Acme Pay helps marketplace teams reason about:

- payment intents
- provider charge routing
- idempotency and duplicate-charge prevention
- double-entry ledger records
- refunds
- provider webhooks
- merchant risk review
- audit events
- payout and provider-outage operations

This is not a real payment processor and should not be used in production.

## Repository Map

```text
src/acme_pay/        Core Python package
tests/              Unit tests for payment, webhook, and risk behavior
docs/architecture/  System design, API contract, ADRs, and .lensignore policy
docs/security/      Security model, threat model, and audit-event expectations
docs/runbooks/      Operator procedures for payout, webhook, provider, risk, and ledger issues
docs/incidents/     Fictional incidents for investigation demos
docs/product/       Personas, roadmap, non-goals, and suggested demo questions
docs/support/       Support macros and investigation notes
examples/api/       Request and response payload examples
examples/issues/    Example backlog items
fixtures/           Noisy fixture content excluded by .lensignore
infra/              Example schema, metrics, and dashboard notes
```

## Try It With Releap

Good questions to ask Releap about this repository:

- How does Acme Pay prevent duplicate charges?
- Where are refunds recorded in the ledger?
- What happens if the payment provider sends the same webhook twice?
- Which security gaps would block a production launch?
- Why is provider fallback routing not automatic?
- Which risk signals can block a merchant payout?
- What code and docs mention audit events for refunds?
- Which database constraints are required for duplicate prevention?
- Why does `.lensignore` exclude provider dump fixtures?

For a fuller evaluation checklist, see `docs/product/demo-query-pack.md`.

## Local Test Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

