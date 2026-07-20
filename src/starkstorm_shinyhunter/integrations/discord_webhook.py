from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from dataclasses import dataclass
from enum import Enum


class ShinyEvent(str, Enum):
    FOUND = "SHINY_FOUND"
    SECURED = "SHINY_SECURED"
    AT_RISK = "SHINY_AT_RISK"


@dataclass(frozen=True, slots=True)
class DiscordMessage:
    event: ShinyEvent
    title: str
    description: str
    fields: tuple[tuple[str, str], ...] = ()

    def payload(self) -> dict:
        return {
            "username": "StarkStormShinyHunter",
            "embeds": [
                {
                    "title": f"{self.event.value} — {self.title}",
                    "description": self.description,
                    "fields": [
                        {"name": name, "value": value, "inline": True}
                        for name, value in self.fields
                    ],
                }
            ],
        }


def send_webhook(message: DiscordMessage, *, timeout: float = 10.0) -> None:
    """Send a Discord webhook event.

    The webhook URL is read only from the environment. It must never be stored in
    source control or logs.
    """
    url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not url:
        raise RuntimeError("DISCORD_WEBHOOK_URL is not configured")

    body = json.dumps(message.payload()).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json", "User-Agent": "StarkStormShinyHunter/0.1"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            if response.status not in {200, 204}:
                raise RuntimeError(f"Discord webhook returned HTTP {response.status}")
    except urllib.error.URLError as exc:
        raise RuntimeError("Discord webhook delivery failed") from exc
