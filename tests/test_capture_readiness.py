import pytest

from starkstorm_shinyhunter.capture_readiness import (
    CaptureReadinessReport,
    CaptureRisk,
    ReadinessStatus,
    critical_encounter_requires_pass,
)


def test_ready_target_passes():
    report = CaptureReadinessReport(
        target="Rayquaza",
        game="Emerald",
        team_can_tank=True,
        hp_control_ready=True,
        status_control_ready=True,
        ball_stock_ready=True,
        checkpoint_ready=True,
        risks=[CaptureRisk("self_ko", True)],
    )
    assert report.status is ReadinessStatus.PASS
    assert report.blockers == []
    report.require_pass()


def test_unmitigated_risk_fails_closed():
    report = CaptureReadinessReport(
        target="Rayquaza",
        game="Emerald",
        team_can_tank=True,
        hp_control_ready=True,
        status_control_ready=True,
        ball_stock_ready=True,
        checkpoint_ready=True,
        risks=[CaptureRisk("pp_exhaustion", False, "Struggle not bounded")],
    )
    assert report.status is ReadinessStatus.FAIL
    assert "pp_exhaustion" in report.blockers
    with pytest.raises(RuntimeError):
        report.require_pass()


def test_critical_encounters_require_gate():
    for kind in ("legendary", "roamer", "safari", "one_time", "critical"):
        assert critical_encounter_requires_pass(kind)
    assert not critical_encounter_requires_pass("ordinary_wild")
