from __future__ import annotations

from hashlib import sha256

from acme_pay.models import Money
from acme_pay.providers.base import ChargeResult


class SandboxProvider:
    """Deterministic provider for local demos and tests."""

    def charge(self, *, amount: Money, payment_method_token: str, idempotency_key: str) -> ChargeResult:
        if payment_method_token.endswith("_decline"):
            return ChargeResult(
                provider_charge_id=self._charge_id(idempotency_key),
                approved=False,
                decline_code="card_declined",
            )
        return ChargeResult(provider_charge_id=self._charge_id(idempotency_key), approved=True)

    def _charge_id(self, idempotency_key: str) -> str:
        digest = sha256(idempotency_key.encode("utf-8")).hexdigest()[:18]
        return f"ch_sandbox_{digest}"

