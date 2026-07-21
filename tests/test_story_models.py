import pytest

from starkstorm_shinyhunter.story.models import (
    LegendaryAccessPath,
    RouteNode,
    StoryRequirement,
    StoryState,
    TriggerSafety,
)


def test_access_path_requires_exactly_one_pre_hunt_stop():
    path = LegendaryAccessPath(
        game="emerald",
        target="Rayquaza",
        encounter_type="static",
        nodes=(
            RouteNode("sky_pillar_entry", "Enter Sky Pillar"),
            RouteNode("rayquaza_trigger", "Interact with Rayquaza", TriggerSafety.PRE_HUNT_STOP),
        ),
        master_save_node_id="rayquaza_trigger",
    )
    assert path.pre_hunt_stop().node_id == "rayquaza_trigger"

    invalid = LegendaryAccessPath(
        game="emerald",
        target="Rayquaza",
        encounter_type="static",
        nodes=(RouteNode("entry", "Entry"),),
        master_save_node_id="entry",
    )
    with pytest.raises(ValueError):
        invalid.pre_hunt_stop()


def test_story_state_requirement_and_grant():
    state = StoryState(game="emerald", flags={"badge_count": 7})
    req = StoryRequirement("badge_count", 7)
    assert state.satisfies(req)
    state.apply((StoryRequirement("sky_pillar_unlocked", True),))
    assert state.flags["sky_pillar_unlocked"] is True
