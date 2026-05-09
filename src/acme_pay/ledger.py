from __future__ import annotations

from collections import defaultdict

from acme_pay.models import LedgerEntry, LedgerSide, Money


class Ledger:
    def __init__(self) -> None:
        self._entries: list[LedgerEntry] = []

    @property
    def entries(self) -> tuple[LedgerEntry, ...]:
        return tuple(self._entries)

    def record_charge(self, merchant_id: str, amount: Money, payment_intent_id: str) -> None:
        self._append_balanced(
            [
                LedgerEntry(f"merchant:{merchant_id}:receivable", LedgerSide.DEBIT, amount, payment_intent_id),
                LedgerEntry("platform:clearing", LedgerSide.CREDIT, amount, payment_intent_id),
            ]
        )

    def record_refund(self, merchant_id: str, amount: Money, refund_id: str) -> None:
        self._append_balanced(
            [
                LedgerEntry("platform:clearing", LedgerSide.DEBIT, amount, refund_id),
                LedgerEntry(f"merchant:{merchant_id}:receivable", LedgerSide.CREDIT, amount, refund_id),
            ]
        )

    def balance_by_account(self) -> dict[str, int]:
        balances: dict[str, int] = defaultdict(int)
        for entry in self._entries:
            direction = 1 if entry.side == LedgerSide.DEBIT else -1
            balances[entry.account] += direction * entry.amount.amount_cents
        return dict(balances)

    def _append_balanced(self, entries: list[LedgerEntry]) -> None:
        debit_total = sum(e.amount.amount_cents for e in entries if e.side == LedgerSide.DEBIT)
        credit_total = sum(e.amount.amount_cents for e in entries if e.side == LedgerSide.CREDIT)
        if debit_total != credit_total:
            raise ValueError("ledger entries must balance")
        self._entries.extend(entries)

