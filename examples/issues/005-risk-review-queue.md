# Add risk review queue

## Background

`MerchantRiskEngine` can return `review` or `block`, but there is no queue for Trust and Safety reviewers.

## Acceptance Criteria

- Persist risk assessments.
- Add a review queue model with reviewer assignment.
- Require audit events for manual overrides.
- Add runbook steps for clearing a false positive.

