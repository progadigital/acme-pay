# Security Model

Acme Pay is designed to keep sensitive card data outside the application boundary. Merchants send provider-issued payment method tokens, not raw PAN data.

## PCI Scope

In the intended architecture, Acme Pay is eligible for a reduced PCI scope because it does not store, process, or transmit raw card numbers. The system still handles payment tokens, merchant identifiers, refund reasons, and provider event payloads, so access controls and audit logging remain required.

## Controls

- Provider tokens are treated as secrets and never logged.
- Idempotency keys are required for payment creation.
- Webhook handlers must verify provider signatures before accepting events.
- Administrative refunds require audit log entries.
- Production databases must enforce unique constraints for idempotency and webhook event IDs.

## Known Security Gaps

- The demo webhook inbox only deduplicates events; it does not verify signatures.
- The demo service stores state in memory and does not include database-level uniqueness.
- Refund authorization is not modeled.
- Provider credentials are not included in the sample configuration.

## Recommended Launch Criteria

- Add signed webhook verification.
- Add role checks for refund and merchant-risk operations.
- Add audit events for refund creation and provider credential rotation.
- Run dependency scanning in CI.
- Document the incident response path for suspected provider-key exposure.

