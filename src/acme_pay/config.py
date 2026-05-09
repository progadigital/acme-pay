from __future__ import annotations

from dataclasses import dataclass
from os import environ


@dataclass(frozen=True)
class Settings:
    environment: str
    provider: str
    database_url: str
    webhook_signing_secret: str


def load_settings() -> Settings:
    return Settings(
        environment=environ.get("ACME_PAY_ENV", "development"),
        provider=environ.get("ACME_PAY_PROVIDER", "sandbox"),
        database_url=environ.get(
            "ACME_PAY_DATABASE_URL",
            "postgres://acme:acme@localhost:5432/acme_pay",
        ),
        webhook_signing_secret=environ.get("ACME_PAY_WEBHOOK_SIGNING_SECRET", "dev-secret"),
    )

