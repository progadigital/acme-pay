from acme_pay.ledger import Ledger
from acme_pay.models import Money, PaymentStatus
from acme_pay.providers.sandbox import SandboxProvider
from acme_pay.service import PaymentNotRefundableError, PaymentService


def test_create_and_capture_records_ledger_entries() -> None:
    ledger = Ledger()
    service = PaymentService(SandboxProvider(), ledger)

    intent = service.create_and_capture_intent(
        merchant_id="m_123",
        amount=Money(2500),
        payment_method_token="pm_card_visa",
        idempotency_key="order-1001",
    )

    assert intent.status == PaymentStatus.SUCCEEDED
    assert len(ledger.entries) == 2
    assert ledger.balance_by_account()["merchant:m_123:receivable"] == 2500


def test_idempotency_key_returns_existing_intent_without_duplicate_ledger_entry() -> None:
    ledger = Ledger()
    service = PaymentService(SandboxProvider(), ledger)

    first = service.create_and_capture_intent(
        merchant_id="m_123",
        amount=Money(2500),
        payment_method_token="pm_card_visa",
        idempotency_key="order-1001",
    )
    second = service.create_and_capture_intent(
        merchant_id="m_123",
        amount=Money(2500),
        payment_method_token="pm_card_visa",
        idempotency_key="order-1001",
    )

    assert second is first
    assert len(ledger.entries) == 2


def test_declined_payment_does_not_hit_ledger() -> None:
    ledger = Ledger()
    service = PaymentService(SandboxProvider(), ledger)

    intent = service.create_and_capture_intent(
        merchant_id="m_123",
        amount=Money(2500),
        payment_method_token="pm_card_decline",
        idempotency_key="order-1002",
    )

    assert intent.status == PaymentStatus.FAILED
    assert ledger.entries == ()


def test_refund_reverses_merchant_receivable() -> None:
    ledger = Ledger()
    service = PaymentService(SandboxProvider(), ledger)
    intent = service.create_and_capture_intent(
        merchant_id="m_123",
        amount=Money(2500),
        payment_method_token="pm_card_visa",
        idempotency_key="order-1003",
    )

    refund = service.refund(payment_intent_id=intent.id, amount=Money(2500), reason="customer_request")

    assert refund.payment_intent_id == intent.id
    assert intent.status == PaymentStatus.REFUNDED
    assert ledger.balance_by_account()["merchant:m_123:receivable"] == 0


def test_failed_payment_cannot_be_refunded() -> None:
    service = PaymentService(SandboxProvider(), Ledger())
    intent = service.create_and_capture_intent(
        merchant_id="m_123",
        amount=Money(2500),
        payment_method_token="pm_card_decline",
        idempotency_key="order-1004",
    )

    try:
        service.refund(payment_intent_id=intent.id, amount=Money(2500), reason="customer_request")
    except PaymentNotRefundableError:
        return

    raise AssertionError("expected PaymentNotRefundableError")

