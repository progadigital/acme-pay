from acme_pay.webhooks import WebhookEvent, WebhookInbox


def test_webhook_inbox_deduplicates_provider_events() -> None:
    inbox = WebhookInbox()
    event = WebhookEvent(
        provider_event_id="evt_123",
        event_type="charge.succeeded",
        object_id="ch_123",
    )

    assert inbox.should_process(event) is True
    assert inbox.should_process(event) is False

