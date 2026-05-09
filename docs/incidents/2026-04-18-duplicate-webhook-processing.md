# Incident: Duplicate Webhook Processing

Date: 2026-04-18

## Summary

A sandbox deployment processed the same `charge.succeeded` webhook twice after a provider retry. No customer funds moved twice, but the downstream notification worker sent duplicate merchant emails.

## Impact

- 14 duplicate merchant emails
- No duplicate ledger entries
- No duplicate customer charges

## Root Cause

Webhook deduplication existed in the payment path but not in the notification worker path. The worker consumed events after payment state reconciliation and did not check `provider_event_id`.

## Follow-ups

- Move provider event ID deduplication into a shared webhook inbox.
- Add tests for duplicate event delivery.
- Add a dashboard panel for duplicate-suppression counts.

