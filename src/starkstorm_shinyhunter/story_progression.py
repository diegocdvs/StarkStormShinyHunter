from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class SafetyClass(str, Enum):
    SAFE = "SAFE"
    PRE_HUNT_STOP = "PRE_HUNT_STOP"
    IRREVERSIBLE = "IRREVERSIBLE"
    UNKNOWN = "UNKNOWN"


class EvidenceStatus(str, Enum):
    CONFIRMED = "CONFIRMED"
    PARTIAL = "PARTIAL"
    PENDING = "PENDING"
    TESTED = "TESTED"


@dataclass(frozen=True, slots=True)
class StoryNode:
    node_id: str
    objective: str
    safety_class: SafetyClass
    prerequisites: tuple[str, ...] = ()
    actions: tuple[str, ...] = ()
    expected_postconditions: tuple[str, ...] = ()
    protected_encounters: tuple[str, ...] = ()
    evidence_status: EvidenceStatus = EvidenceStatus.PENDING
    source_refs: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class ProgressionContext:
    capture_readiness_passed: bool
    persistent_backup_validated: bool
    observed_prerequisites: frozenset[str] = field(default_factory=frozenset)


@dataclass(frozen=True, slots=True)
class GateDecision:
    allowed: bool
    reasons: tuple[str, ...]


def evaluate_story_gate(node: StoryNode, context: ProgressionContext) -> GateDecision:
    """Fail closed before executing a story node.

    Unknown evidence, unmet prerequisites, hunt stops without capture readiness,
    and irreversible actions without a validated persistent backup are blocked.
    """
    reasons: list[str] = []

    missing = sorted(set(node.prerequisites) - set(context.observed_prerequisites))
    if missing:
        reasons.append("missing prerequisites: " + ", ".join(missing))

    if node.safety_class is SafetyClass.UNKNOWN:
        reasons.append("node safety is UNKNOWN")

    if node.evidence_status is EvidenceStatus.PENDING:
        reasons.append("node evidence is PENDING")

    if node.safety_class is SafetyClass.PRE_HUNT_STOP and not context.capture_readiness_passed:
        reasons.append("Capture Readiness has not passed")

    if node.safety_class is SafetyClass.IRREVERSIBLE and not context.persistent_backup_validated:
        reasons.append("validated persistent backup is required")

    return GateDecision(allowed=not reasons, reasons=tuple(reasons))
