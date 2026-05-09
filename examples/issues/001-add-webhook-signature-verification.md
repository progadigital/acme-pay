# Add provider webhook signature verification

## Background

The webhook inbox currently deduplicates provider events by `provider_event_id`, but it does not prove the event came from the provider.

## Acceptance Criteria

- Reject webhook payloads with missing signatures.
- Reject webhook payloads with invalid signatures.
- Verify timestamp tolerance to reduce replay risk.
- Add tests for valid, invalid, missing, and expired signatures.
- Update `docs/security/security-model.md`.

