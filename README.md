# Acme Pay

Acme Pay is a fictional payments orchestration service used for demos, search examples, and repository-question workflows.

The repo is intentionally small, but it is shaped like a real product codebase. It includes API-oriented domain code, provider adapters, ledger behavior, architecture notes, runbooks, security decisions, sample incidents, and issue prompts that make it useful for testing codebase query tools.

## Product Surface

Acme Pay helps marketplace teams:

- create payment intents for card and bank payments
- route charges to a payment provider
- record double-entry ledger movements
- process refunds
- receive provider webhooks
- review merchant risk status
- audit administrative changes

## Repo Map

```text
src/acme_pay/        Core Python package
docs/architecture/  System design and data-flow notes
docs/security/      Security model and risk tradeoffs
docs/product/       Personas and demo query prompts
docs/support/       Support-facing macros and investigation notes
docs/runbooks/      Operator procedures
docs/incidents/     Fictional production incidents
examples/issues/    Demo-ready GitHub issue bodies
examples/api/       Request and response payload examples
fixtures/           Intentionally noisy files used to demonstrate .lensignore
infra/              Example deployment and schema artifacts
tests/              Unit tests for domain behavior
```

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Demo Questions This Repo Should Answer

- How does Acme Pay prevent duplicate charges?
- Where are refunds recorded in the ledger?
- What happens if the payment provider webhook arrives twice?
- Which parts of the system are in scope for PCI?
- What operational steps should an on-call engineer take when payouts are delayed?
- What are the known security gaps before a real production launch?
- Which API routes require elevated roles?
- What risk signals can block a payout or payment?
- Which design decisions were made for idempotency and ledger storage?
- Why does `.lensignore` exclude provider dump fixtures?

## Extraction Plan

This folder is designed to become its own public repository. Keep all Acme Pay content inside this directory so it can be extracted later with:

```bash
git subtree split --prefix=demo-repos/acme-pay -b acme-pay-public
```
