# Demo Query Pack

Use these prompts when testing Acme Pay as a queryable workspace.

## Golden Prompts

| Prompt | Strong Answer Should Mention |
| --- | --- |
| Why does payment creation require an idempotency key? | Duplicate request retries, `PaymentService.create_and_capture_intent`, unique `payment_intents.idempotency_key`, ADR 0001, and duplicate response payloads. |
| Where would I add webhook signature verification? | Before `WebhookInbox.should_process`, security launch gap, invalid-signature example payload, and ADR 0003 consequence that verification happens before inbox recording. |
| Is the ledger append-only, and how are refunds represented? | ADR 0002, `Ledger.record_refund`, clearing debit, merchant receivable credit, and reversal entries instead of mutation. |
| What happens if the provider sends the same webhook twice? | `WebhookInbox` suppresses duplicate provider event IDs, webhook replay runbook, duplicate incident from 2026-04-18, and `webhook.duplicate_suppressed.count`. |
| Which security gaps block a production launch? | Webhook signature verification, durable uniqueness, refund authorization, audit events, provider credential handling, and dependency scanning. |
| Why is provider fallback routing not automatic? | Provider routing doc, provider outage runbook, fail-closed policy, merchant enrollment, and reconciliation/dispute/refund differences. |
| Which risk signals can block a merchant payout? | `large_payment`, `cross_border_payment_method`, `new_merchant`, risk review runbook, and 2026-05-02 false-positive incident. |
| What code and docs mention audit events for refunds? | `AuditLog`, `docs/security/audit-events.md`, refund API payload actor ID, schema `admin_audit_log`, and issue 003 noting the service gap. |
| Which database constraints are required for duplicate prevention? | Unique `payment_intents.idempotency_key`, primary key `webhook_events.provider_event_id`, and append-only ledger invariants. |
| What should on-call do during a provider outage? | Confirm provider scope, disable non-critical retries, verify idempotency, notify support, avoid fallback unless enrolled, and use the provider outage runbook. |

## Evaluation Notes

A good answer should cite more than one part of the repo when the prompt is cross-cutting. For example, a refund audit answer should connect the schema, security docs, API example, backlog issue, and missing service implementation.

Short answers are fine for direct implementation questions. Risk, launch readiness, and incident questions should surface known gaps and operational consequences.
