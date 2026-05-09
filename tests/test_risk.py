from acme_pay.models import Money
from acme_pay.risk import MerchantRiskEngine, RiskDecision


def test_low_risk_payment_is_approved() -> None:
    result = MerchantRiskEngine().assess_payment(
        merchant_id="m_123",
        amount=Money(2_500),
        payment_method_country="US",
        merchant_country="US",
        merchant_age_days=180,
    )

    assert result.decision == RiskDecision.APPROVE
    assert result.score == 0


def test_new_cross_border_large_payment_is_blocked() -> None:
    result = MerchantRiskEngine().assess_payment(
        merchant_id="m_456",
        amount=Money(150_000),
        payment_method_country="CA",
        merchant_country="US",
        merchant_age_days=3,
    )

    assert result.decision == RiskDecision.BLOCK
    assert {signal.name for signal in result.signals} == {
        "large_payment",
        "cross_border_payment_method",
        "new_merchant",
    }

