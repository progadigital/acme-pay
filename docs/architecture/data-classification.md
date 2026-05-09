# Data Classification

| Data | Classification | Notes |
| --- | --- | --- |
| Raw card number | Prohibited | Must never enter Acme Pay systems |
| Payment method token | Confidential | Tokenized by provider, do not log |
| Provider charge ID | Internal | Safe for support tools |
| Merchant ID | Internal | May appear in logs |
| Refund reason | Confidential | Can contain customer context |
| Risk signal | Confidential | Internal Trust and Safety data |
| Audit event metadata | Confidential | Contains operator and target details |

## Logging Rule

Logs may include payment intent IDs, merchant IDs, provider charge IDs, and stable error codes. Logs must not include raw provider payloads, payment method tokens, or webhook signing secrets.

