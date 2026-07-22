import pytest

from starkstorm_shinyhunter.gen2_shiny import (
    Gen1EncounterClass,
    Gen2DVs,
    gen1_retroactive_shiny_eligible,
)


@pytest.mark.parametrize("attack", [2, 3, 6, 7, 10, 11, 14, 15])
def test_gen2_shiny_attack_dvs(attack):
    assert Gen2DVs(attack, 10, 10, 10).is_shiny


@pytest.mark.parametrize("attack", [0, 1, 4, 5, 8, 9, 12, 13])
def test_gen2_non_shiny_attack_dvs(attack):
    assert not Gen2DVs(attack, 10, 10, 10).is_shiny


def test_other_required_dvs_must_equal_ten():
    assert not Gen2DVs(2, 9, 10, 10).is_shiny
    assert not Gen2DVs(2, 10, 9, 10).is_shiny
    assert not Gen2DVs(2, 10, 10, 9).is_shiny


@pytest.mark.parametrize(
    "encounter_class",
    [
        Gen1EncounterClass.FISHING,
        Gen1EncounterClass.GIFT,
        Gen1EncounterClass.STATIC,
        Gen1EncounterClass.INGAME_TRADE,
    ],
)
def test_gen1_supported_classes_can_be_retroactive_shiny(encounter_class):
    assert gen1_retroactive_shiny_eligible(encounter_class, Gen2DVs(10, 10, 10, 10))


@pytest.mark.parametrize(
    "encounter_class",
    [Gen1EncounterClass.GRASS, Gen1EncounterClass.CAVE, Gen1EncounterClass.SURF, Gen1EncounterClass.OTHER],
)
def test_gen1_unsupported_classes_fail_closed(encounter_class):
    assert not gen1_retroactive_shiny_eligible(encounter_class, Gen2DVs(10, 10, 10, 10))


def test_dv_range_validation():
    with pytest.raises(ValueError):
        Gen2DVs(16, 10, 10, 10)
