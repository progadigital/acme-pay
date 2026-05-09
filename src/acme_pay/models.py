from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from uuid import uuid4


class Currency(str, Enum):
    USD = "USD"
    EUR = "EUR"


class PaymentStatus(str, Enum):
    REQUIRES_CAPTURE = "requires_capture"
    SUCCEEDED = "succeeded"
    REFUNDED = "refunded"
    FAILED = "failed"


class LedgerSide(str, Enum):
    DEBIT = "debit"
    CREDIT = "credit"


@dataclass(frozen=True)
class Money:
    amount_cents: int
    currency: Currency = Currency.USD

    def __post_init__(self) -> None:
        if self.amount_cents <= 0:
            raise ValueError("amount_cents must be positive")


@dataclass
class PaymentIntent:
    merchant_id: str
    amount: Money
    idempotency_key: str
    payment_method_token: str
    id: str = field(default_factory=lambda: f"pi_{uuid4().hex[:18]}")
    status: PaymentStatus = PaymentStatus.REQUIRES_CAPTURE
    provider_charge_id: str | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass(frozen=True)
class LedgerEntry:
    account: str
    side: LedgerSide
    amount: Money
    source_id: str
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass
class Refund:
    payment_intent_id: str
    amount: Money
    reason: str
    id: str = field(default_factory=lambda: f"rf_{uuid4().hex[:18]}")
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
