from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class TriggerSafety(str, Enum):
    SAFE = "SAFE"
    PRE_HUNT_STOP = "PRE_HUNT_STOP"
    IRREVERSIBLE = "IRREVERSIBLE"


@dataclass(frozen=True, slots=True)
class StoryRequirement:
    key: str
    value: str | int | bool = True


@dataclass(frozen=True, slots=True)
class RouteNode:
    node_id: str
    description: str
    safety: TriggerSafety = TriggerSafety.SAFE
    requirements: tuple[StoryRequirement, ...] = ()
    grants: tuple[StoryRequirement, ...] = ()
    evidence_status: str = "PENDING"
    source_ref: str | None = None


@dataclass(frozen=True, slots=True)
class LegendaryAccessPath:
    game: str
    target: str
    encounter_type: str
    nodes: tuple[RouteNode, ...]
    master_save_node_id: str
    notes: tuple[str, ...] = ()

    def pre_hunt_stop(self) -> RouteNode:
        stops = [n for n in self.nodes if n.safety is TriggerSafety.PRE_HUNT_STOP]
        if len(stops) != 1:
            raise ValueError("LegendaryAccessPath must contain exactly one PRE_HUNT_STOP")
        return stops[0]


@dataclass(slots=True)
class StoryState:
    game: str
    flags: dict[str, str | int | bool] = field(default_factory=dict)
    current_node_id: str | None = None

    def satisfies(self, requirement: StoryRequirement) -> bool:
        return self.flags.get(requirement.key) == requirement.value

    def apply(self, grants: tuple[StoryRequirement, ...]) -> None:
        for grant in grants:
            self.flags[grant.key] = grant.value
