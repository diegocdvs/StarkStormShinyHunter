from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class BallPolicy(str, Enum):
    FORCED_MECHANIC = "forced_mechanic"
    HGSS_APRIBALL_CONFIRMATION = "hgss_apriball_confirmation"
    LUXURY = "luxury_ball"
    POKE = "poke_ball"


@dataclass(frozen=True, slots=True)
class CaptureContext:
    game: str
    forced_ball: str | None = None
    luxury_ball_available: bool = True


def choose_ball_policy(context: CaptureContext) -> BallPolicy:
    """Select the policy layer; never silently substitute a more efficient ball."""
    if context.forced_ball:
        return BallPolicy.FORCED_MECHANIC
    if context.game.strip().lower() in {"heartgold", "soulsilver", "hg", "ss", "hgss"}:
        return BallPolicy.HGSS_APRIBALL_CONFIRMATION
    if context.luxury_ball_available:
        return BallPolicy.LUXURY
    return BallPolicy.POKE
