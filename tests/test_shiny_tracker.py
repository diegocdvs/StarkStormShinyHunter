import pytest

from starkstorm_shinyhunter.shiny_tracker import (
    ShinyLivingDexTracker,
    ShinySpecimen,
    TrackerStatus,
)


def specimen(dex: int, species: str, *, form: str = "default") -> ShinySpecimen:
    return ShinySpecimen(
        national_dex=dex,
        species=species,
        form=form,
        game="Pokémon Emerald",
        save_id="Emerald_Diego_01.sav",
        ball="Luxury Ball",
        method="RNG",
    )


def test_register_completes_standard_slot_and_clears_hunting() -> None:
    tracker = ShinyLivingDexTracker.from_species([(384, "Rayquaza")])
    tracker.mark_hunting(384)

    slot = tracker.register(specimen(384, "Rayquaza"))

    assert slot.status is TrackerStatus.CAUGHT
    assert slot.hunting is False
    assert tracker.completed_slots == 1
    assert tracker.completion_ratio == 1.0


def test_required_forms_are_independent_completion_requirements() -> None:
    tracker = ShinyLivingDexTracker.from_species(
        [(201, "Unown")], required_forms={201: ("A", "B", "C")}
    )

    tracker.register(specimen(201, "Unown", form="A"))
    tracker.register(specimen(201, "Unown", form="B"))

    slot = tracker.slots[201]
    assert slot.is_complete is False
    assert slot.missing_forms == ("C",)

    tracker.register(specimen(201, "Unown", form="C"))
    assert slot.is_complete is True


def test_duplicate_count_excludes_one_specimen_per_required_form() -> None:
    tracker = ShinyLivingDexTracker.from_species([(25, "Pikachu")])
    tracker.register(specimen(25, "Pikachu"))
    tracker.register(specimen(25, "Pikachu"))

    assert tracker.duplicate_count == 1


def test_species_mismatch_fails_closed() -> None:
    tracker = ShinyLivingDexTracker.from_species([(1, "Bulbasaur")])

    with pytest.raises(ValueError, match="Species mismatch"):
        tracker.register(specimen(1, "Charmander"))


def test_summary_tracks_hunts_without_counting_completed_slot_as_hunting() -> None:
    tracker = ShinyLivingDexTracker.from_species([(1, "Bulbasaur"), (2, "Ivysaur")])
    tracker.mark_hunting(1)
    tracker.mark_hunting(2)
    tracker.register(specimen(1, "Bulbasaur"))

    assert tracker.summary() == {
        "completed": 1,
        "total": 2,
        "completion_ratio": 0.5,
        "hunting": 1,
        "duplicates": 0,
    }
