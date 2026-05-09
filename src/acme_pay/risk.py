from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from acme_pay.models import Money


class RiskDecision(str, Enum):
    APPROVE = "approve"
    REVIEW = "review"
    BLOCK = "block"


@dataclass(frozen=True)
class RiskSignal:
    name: str
    value: str
    weight: int


@dataclass(frozen=True)
class RiskAssessment:
    merchant_id: str
    decision: RiskDecision
    score: int
    signals: tuple[RiskSignal, ...]


class MerchantRiskEngine:
    def assess_payment(
        self,
        *,
        merchant_id: str,
        amount: Money,
        payment_method_country: str,
        merchant_country: str,
        merchant_age_days: int,
    ) -> RiskAssessment:
        signals: list[RiskSignal] = []

        if amount.amount_cents >= 100_000:
            signals.append(RiskSignal("large_payment", str(amount.amount_cents), 35))
        if payment_method_country != merchant_country:
            signals.append(RiskSignal("cross_border_payment_method", payment_method_country, 25))
        if merchant_age_days < 14:
            signals.append(RiskSignal("new_merchant", str(merchant_age_days), 30))

        score = sum(signal.weight for signal in signals)
        if score >= 70:
            decision = RiskDecision.BLOCK
        elif score >= 35:
            decision = RiskDecision.REVIEW
        else:
            decision = RiskDecision.APPROVE

        return RiskAssessment(
            merchant_id=merchant_id,
            decision=decision,
            score=score,
            signals=tuple(signals),
        )

