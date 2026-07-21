from starkstorm_shinyhunter.story.progression import (
    LegendaryAccessPath,
    StoryRequirement,
    StoryState,
    TriggerClass,
    may_cross_trigger,
)


def test_story_requirements_report_missing_items():
    path = LegendaryAccessPath(
        target="Example Legendary",
        game="Emerald",
        minimum_story_milestone="late_game",
        requirements=(
            StoryRequirement("badge_1", "First badge"),
            StoryRequirement("key_event", "Required story event"),
        ),
    )
    state = StoryState(completed={"badge_1"})
    assert not state.satisfies(path)
    assert [item.key for item in state.missing(path)] == ["key_event"]


def test_safe_trigger_can_be_crossed_without_hunt_setup():
    assert may_cross_trigger(
        trigger=TriggerClass.SAFE,
        capture_readiness_passed=False,
        backup_created=False,
    )


def test_pre_hunt_stop_requires_readiness_and_backup():
    assert not may_cross_trigger(
        trigger=TriggerClass.PRE_HUNT_STOP,
        capture_readiness_passed=True,
        backup_created=False,
    )
    assert may_cross_trigger(
        trigger=TriggerClass.PRE_HUNT_STOP,
        capture_readiness_passed=True,
        backup_created=True,
    )


def test_critical_trigger_is_never_crossed_by_generic_progression():
    assert not may_cross_trigger(
        trigger=TriggerClass.CRITICAL_TRIGGER,
        capture_readiness_passed=True,
        backup_created=True,
    )
