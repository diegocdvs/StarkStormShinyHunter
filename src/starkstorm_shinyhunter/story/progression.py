from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class TriggerClass(str, Enum):
    SAFE = "safe"
    PRE_HUNT_STOP = "pre_hunt_stop"
    CRITICAL_TRIGGER = "critical_trigger"


@dataclass(frozen=True, slots=True)
class StoryRequirement:
    key: str
    description: str


@dataclass(frozen=True, slots=True)
class LegendaryAccessPath:
    target: str
    game: str
    minimum_story_milestone: str
    requirements: tuple[StoryRequirement, ...] = ()
    route_steps: tuple[str, ...] = ()
    encounter_class: str = "static"
    trigger_class: TriggerClass = TriggerClass.PRE_HUNT_STOP
    master_pre_hunt_save_hint: str | None = None
    notes: tuple[str, ...] = ()


@dataclass(slots=True)
class StoryState:
    completed: set[str] = field(default_factory=set)

    def satisfies(self, path: LegendaryAccessPath) -> bool:
        return all(req.key in self.completed for req in path.requirements)

    def missing(self, path: LegendaryAccessPath) -> tuple[StoryRequirement, ...]:
        return tuple(req for req in path.requirements if req.key not in self.completed)


def may_cross_trigger(*, trigger: TriggerClass, capture_readiness_passed: bool, backup_created: bool) -> bool:
    if trigger is TriggerClass.SAFE:
        return True
    if trigger is TriggerClass.PRE_HUNT_STOP:
        return capture_readiness_passed and backup_created
    return False
