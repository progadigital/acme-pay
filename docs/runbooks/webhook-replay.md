# Runbook: Webhook Replay

Use this runbook when provider webhook delivery is delayed or when events need to be replayed.

## Safe Replay Conditions

- Provider event IDs are stable.
- The webhook inbox has a unique record per provider event ID.
- Event handlers are idempotent.

## Procedure

1. Identify the missing provider event IDs.
2. Confirm the events have valid provider signatures.
3. Replay events in chronological order.
4. Monitor duplicate-suppression counts in the webhook inbox.
5. Compare payment intent state with provider charge state.

## Caution

Do not replay unsigned payloads from support tickets or chat transcripts. Fetch replay payloads directly from the payment provider dashboard or API.

