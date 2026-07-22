"""Generation I/II DV-based shiny primitives.

Pure domain logic only. Emulator-specific memory extraction belongs in adapters.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

SHINY_ATTACK_DVS = frozenset({2, 3, 6, 7, 10, 11, 14, 15})


@dataclass(frozen=True, slots=True)
class Gen2DVs:
    attack: int
    defense: int
    speed: int
    special: int

    def __post_init__(self) -> None:
        for name, value in (
            ("attack", self.attack),
            ("defense", self.defense),
            ("speed", self.speed),
            ("special", self.special),
        ):
            if not 0 <= value <= 15:
                raise ValueError(f"{name} DV must be between 0 and 15")

    @property
    def is_shiny(self) -> bool:
        return (
            self.defense == 10
            and self.speed == 10
            and self.special == 10
            and self.attack in SHINY_ATTACK_DVS
        )


class Gen1EncounterClass(str, Enum):
    GRASS = "grass"
    CAVE = "cave"
    SURF = "surf"
    FISHING = "fishing"
    GIFT = "gift"
    STATIC = "static"
    INGAME_TRADE = "ingame_trade"
    OTHER = "other"


RETROACTIVE_ELIGIBLE_CLASSES = frozenset(
    {
        Gen1EncounterClass.FISHING,
        Gen1EncounterClass.GIFT,
        Gen1EncounterClass.STATIC,
        Gen1EncounterClass.INGAME_TRADE,
    }
)


def gen1_retroactive_shiny_eligible(
    encounter_class: Gen1EncounterClass,
    dvs: Gen2DVs,
) -> bool:
    """Conservative eligibility gate for a Gen I -> Gen II retroactive shiny.

    Ordinary grass/cave/Surf generators are deliberately fail-closed because
    their Gen I RNG correlations prevent the Gen-II shiny DV combination.
    """

    return encounter_class in RETROACTIVE_ELIGIBLE_CLASSES and dvs.is_shiny
