from pathlib import Path

import pytest

from starkstorm_shinyhunter.domain.checkpoints import Checkpoint, CheckpointKind
from starkstorm_shinyhunter.domain.policies import BallPolicy, CaptureContext, choose_ball_policy
from starkstorm_shinyhunter.domain.readiness import CaptureReadiness


def test_ball_policy_precedence() -> None:
    assert choose_ball_policy(CaptureContext(game="Emerald", forced_ball="Safari Ball")) is BallPolicy.FORCED_MECHANIC
    assert choose_ball_policy(CaptureContext(game="HeartGold")) is BallPolicy.HGSS_APRIBALL_CONFIRMATION
    assert choose_ball_policy(CaptureContext(game="Emerald", luxury_ball_available=True)) is BallPolicy.LUXURY
    assert choose_ball_policy(CaptureContext(game="Emerald", luxury_ball_available=False)) is BallPolicy.POKE


def test_encounter_raw_must_be_immutable() -> None:
    cp = Checkpoint(
        kind=CheckpointKind.ENCOUNTER_RAW,
        path=Path("raw.state"),
        sha256="0" * 64,
        immutable=False,
    )
    with pytest.raises(ValueError):
        cp.validate()


def test_capture_readiness_requires_all_gates() -> None:
    readiness = CaptureReadiness(
        team_survivability=True,
        hp_control=True,
        status_control=True,
        escape_or_selfko_control=True,
        ball_stock=True,
        pp_struggle_margin=False,
        save_checkpoint_ready=True,
        notes=["PP/Struggle margin insufficient"],
    )
    assert not readiness.passed
    with pytest.raises(RuntimeError):
        readiness.require_pass()
