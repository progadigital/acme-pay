from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Route:
    method: str
    path: str
    summary: str
    required_role: str


ROUTES = (
    Route("POST", "/v1/payment_intents", "Create and capture a payment intent", "merchant:write"),
    Route("POST", "/v1/refunds", "Create a refund for a succeeded payment", "refund:write"),
    Route("POST", "/v1/webhooks/provider", "Receive provider webhook events", "provider:webhook"),
    Route("GET", "/v1/merchants/{merchant_id}/risk", "Inspect merchant risk status", "risk:read"),
    Route("GET", "/v1/audit_events", "Search administrative audit events", "audit:read"),
)


def route_summaries() -> list[str]:
    return [f"{route.method} {route.path} - {route.summary}" for route in ROUTES]

