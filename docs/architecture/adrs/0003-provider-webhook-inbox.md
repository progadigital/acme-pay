# ADR 0003: Deduplicate Provider Webhooks in an Inbox

Status: Accepted

## Context

Payment providers retry webhooks during network failures and timeout windows. Replayed events should not create duplicate notifications, ledger movements, or state transitions.

## Decision

Acme Pay records each provider event ID in a webhook inbox before dispatching business handlers. Duplicate event IDs are skipped.

## Consequences

- The `webhook_events.provider_event_id` column must be unique.
- Replay tooling can safely submit the same event more than once.
- Signature verification must happen before an event is recorded as processed.

