# Add admin audit events for refunds

## Background

Refund creation should be visible in the admin audit log. The schema includes `admin_audit_log`, but the application service does not write audit events yet.

## Acceptance Criteria

- Add an audit writer abstraction.
- Record actor ID, refund ID, payment intent ID, merchant ID, and reason.
- Tests prove refunds cannot be created without an actor ID.
- Update the security model with the new control.

