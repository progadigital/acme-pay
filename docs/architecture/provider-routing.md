# Provider Routing

Acme Pay currently ships with a deterministic sandbox provider. Production routing is expected to choose a provider based on merchant region, currency, method type, and provider health.

## Routing Inputs

- Merchant country
- Settlement currency
- Payment method type
- Provider availability
- Merchant risk tier

## Routing Policy

Initial routing should prefer the primary card processor for US card payments and a regional processor for EUR payments. If the primary processor is degraded, new payment intents should fail closed unless the merchant is explicitly enabled for fallback routing.

## Why Fail Closed?

Failing closed avoids silent differences in dispute handling, settlement timing, and refund semantics. A fallback processor can be safer after merchant contract, reconciliation, and support processes are ready.

## Query Signal

Questions about "why don't we automatically route around provider outages?" should land here and in `docs/runbooks/provider-outage.md`.

