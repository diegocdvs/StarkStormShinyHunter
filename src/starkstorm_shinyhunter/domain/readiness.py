from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class CaptureReadiness:
    team_survivability: bool
    hp_control: bool
    status_control: bool
    escape_or_selfko_control: bool
    ball_stock: bool
    pp_struggle_margin: bool
    save_checkpoint_ready: bool
    notes: list[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return all(
            (
                self.team_survivability,
                self.hp_control,
                self.status_control,
                self.escape_or_selfko_control,
                self.ball_stock,
                self.pp_struggle_margin,
                self.save_checkpoint_ready,
            )
        )

    def require_pass(self) -> None:
        if not self.passed:
            detail = "; ".join(self.notes) if self.notes else "one or more readiness gates failed"
            raise RuntimeError(f"Capture Readiness failed: {detail}")
