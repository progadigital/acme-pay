from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from acme_pay.models import Money


@dataclass(frozen=True)
class ChargeResult:
    provider_charge_id: str
    approved: bool
    decline_code: str | None = None


class PaymentProvider(Protocol):
    def charge(self, *, amount: Money, payment_method_token: str, idempotency_key: str) -> ChargeResult:
        """Create a provider charge using the caller's idempotency key."""

