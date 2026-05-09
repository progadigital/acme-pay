# Runbook: Provider Outage

Use this runbook when the active payment provider is degraded or unavailable.

## Symptoms

- Elevated provider timeout rate
- Increased `payment_intent.failed` count
- Merchant support reports of checkout failures
- Provider status page incident

## Immediate Actions

1. Confirm whether the provider is failing globally or for a region.
2. Disable non-critical retries that can increase duplicate request volume.
3. Confirm idempotency keys are present on merchant retry traffic.
4. Notify support with affected payment method types and regions.
5. Do not enable fallback routing unless the merchant is enrolled for it.

## Fallback Routing

Fallback routing is not automatic. The provider-routing ADR prefers fail-closed behavior until reconciliation, disputes, and refund behavior are validated for a merchant.

