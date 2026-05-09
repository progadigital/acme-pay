from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class WebhookEvent:
    provider_event_id: str
    event_type: str
    object_id: str


class WebhookInbox:
    def __init__(self) -> None:
        self._processed_event_ids: set[str] = set()

    def should_process(self, event: WebhookEvent) -> bool:
        if event.provider_event_id in self._processed_event_ids:
            return False
        self._processed_event_ids.add(event.provider_event_id)
        return True

