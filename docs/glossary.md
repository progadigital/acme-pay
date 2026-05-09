# Glossary

## Payment Intent

An Acme Pay record representing an attempt to collect money from a customer for a merchant.

## Idempotency Key

A merchant-provided key that makes payment creation safe to retry. The same key should return the same payment intent.

## Provider Charge ID

The external processor's identifier for a charge. It is useful for support and reconciliation but is not the primary source of Acme Pay state.

## Clearing Account

Ledger account used while money is in transit between provider settlement and merchant receivable accounting.

## Webhook Inbox

Storage layer that records provider event IDs before business handlers run, preventing duplicate event processing.

## Risk Override

Manual Trust and Safety decision that changes the result of a risk assessment. Overrides must be audited.

