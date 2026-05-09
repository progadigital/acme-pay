# Incident: Risk False Positive for New Merchant

Date: 2026-05-02

## Summary

A newly onboarded merchant had a high-value payment blocked because the risk engine combined `large_payment`, `cross_border_payment_method`, and `new_merchant` signals. The payment was legitimate, but there was no review queue or audited override path.

## Impact

- 1 merchant checkout blocked for 42 minutes
- No funds lost
- Support handled the case manually

## Root Cause

The risk engine returned `block`, but the product had not yet implemented a Trust and Safety review queue or override workflow.

## Follow-ups

- Build a risk review queue.
- Require audit events for risk overrides.
- Add support macros for explaining temporary risk holds.

