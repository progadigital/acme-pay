from __future__ import annotations

from acme_pay.ledger import Ledger
from acme_pay.models import Money, PaymentIntent, PaymentStatus, Refund
from acme_pay.providers.base import PaymentProvider


class DuplicateIntentError(Exception):
    pass


class PaymentNotRefundableError(Exception):
    pass


class PaymentService:
    def __init__(self, provider: PaymentProvider, ledger: Ledger) -> None:
        self.provider = provider
        self.ledger = ledger
        self._intents_by_idempotency_key: dict[str, PaymentIntent] = {}
        self._intents_by_id: dict[str, PaymentIntent] = {}

    def create_and_capture_intent(
        self,
        *,
        merchant_id: str,
        amount: Money,
        payment_method_token: str,
        idempotency_key: str,
    ) -> PaymentIntent:
        existing = self._intents_by_idempotency_key.get(idempotency_key)
        if existing is not None:
            return existing

        intent = PaymentIntent(
            merchant_id=merchant_id,
            amount=amount,
            payment_method_token=payment_method_token,
            idempotency_key=idempotency_key,
        )
        result = self.provider.charge(
            amount=amount,
            payment_method_token=payment_method_token,
            idempotency_key=idempotency_key,
        )
        intent.provider_charge_id = result.provider_charge_id
        intent.status = PaymentStatus.SUCCEEDED if result.approved else PaymentStatus.FAILED

        self._intents_by_idempotency_key[idempotency_key] = intent
        self._intents_by_id[intent.id] = intent

        if intent.status == PaymentStatus.SUCCEEDED:
            self.ledger.record_charge(merchant_id, amount, intent.id)

        return intent

    def refund(self, *, payment_intent_id: str, amount: Money, reason: str) -> Refund:
        intent = self._intents_by_id[payment_intent_id]
        if intent.status != PaymentStatus.SUCCEEDED:
            raise PaymentNotRefundableError(f"payment intent {payment_intent_id} is not refundable")
        if amount.amount_cents > intent.amount.amount_cents:
            raise PaymentNotRefundableError("refund cannot exceed original payment amount")

        refund = Refund(payment_intent_id=payment_intent_id, amount=amount, reason=reason)
        intent.status = PaymentStatus.REFUNDED
        self.ledger.record_refund(intent.merchant_id, amount, refund.id)
        return refund

