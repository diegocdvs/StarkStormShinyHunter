from dataclasses import dataclass, field
from enum import Enum


class ReadinessStatus(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"


@dataclass(frozen=True)
class CaptureRisk:
    name: str
    mitigated: bool
    detail: str = ""


@dataclass
class CaptureReadinessReport:
    target: str
    game: str
    team_can_tank: bool
    hp_control_ready: bool
    status_control_ready: bool
    ball_stock_ready: bool
    checkpoint_ready: bool
    risks: list[CaptureRisk] = field(default_factory=list)

    @property
    def blockers(self) -> list[str]:
        blockers: list[str] = []
        if not self.team_can_tank:
            blockers.append("team_survivability")
        if not self.hp_control_ready:
            blockers.append("hp_control")
        if not self.status_control_ready:
            blockers.append("status_control")
        if not self.ball_stock_ready:
            blockers.append("ball_stock")
        if not self.checkpoint_ready:
            blockers.append("checkpoint")
        blockers.extend(r.name for r in self.risks if not r.mitigated)
        return blockers

    @property
    def status(self) -> ReadinessStatus:
        return ReadinessStatus.PASS if not self.blockers else ReadinessStatus.FAIL

    def require_pass(self) -> None:
        if self.status is ReadinessStatus.FAIL:
            raise RuntimeError(
                "Capture Readiness failed: " + ", ".join(self.blockers)
            )


def critical_encounter_requires_pass(encounter_kind: str) -> bool:
    """Fail closed for encounter classes where losing the target is costly."""
    return encounter_kind.lower() in {
        "legendary",
        "roamer",
        "safari",
        "one_time",
        "critical",
    }
