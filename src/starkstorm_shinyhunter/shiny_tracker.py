from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import date
from enum import StrEnum
from typing import Iterable


class TrackerStatus(StrEnum):
    MISSING = "missing"
    HUNTING = "hunting"
    CAUGHT = "caught"


@dataclass(slots=True)
class ShinySpecimen:
    national_dex: int
    species: str
    game: str
    save_id: str
    ball: str
    method: str
    caught_on: str = field(default_factory=lambda: date.today().isoformat())
    location: str = ""
    form: str = "default"
    gender: str | None = None
    nature: str | None = None
    pid: str | None = None
    notes: str = ""

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(slots=True)
class LivingDexSlot:
    national_dex: int
    species: str
    required_forms: tuple[str, ...] = ("default",)
    specimens: list[ShinySpecimen] = field(default_factory=list)
    hunting: bool = False

    @property
    def status(self) -> TrackerStatus:
        if self.is_complete:
            return TrackerStatus.CAUGHT
        return TrackerStatus.HUNTING if self.hunting else TrackerStatus.MISSING

    @property
    def owned_forms(self) -> set[str]:
        return {s.form for s in self.specimens}

    @property
    def missing_forms(self) -> tuple[str, ...]:
        owned = self.owned_forms
        return tuple(form for form in self.required_forms if form not in owned)

    @property
    def is_complete(self) -> bool:
        return not self.missing_forms

    @property
    def duplicate_count(self) -> int:
        # One specimen per required form contributes to completion; extras are duplicates.
        useful = sum(1 for form in self.required_forms if form in self.owned_forms)
        return max(0, len(self.specimens) - useful)


@dataclass(slots=True)
class ShinyLivingDexTracker:
    slots: dict[int, LivingDexSlot]

    @classmethod
    def from_species(
        cls,
        species: Iterable[tuple[int, str]],
        *,
        required_forms: dict[int, tuple[str, ...]] | None = None,
    ) -> "ShinyLivingDexTracker":
        forms = required_forms or {}
        return cls(
            slots={
                dex: LivingDexSlot(
                    national_dex=dex,
                    species=name,
                    required_forms=forms.get(dex, ("default",)),
                )
                for dex, name in species
            }
        )

    def register(self, specimen: ShinySpecimen) -> LivingDexSlot:
        try:
            slot = self.slots[specimen.national_dex]
        except KeyError as exc:
            raise ValueError(f"Unknown National Dex number: {specimen.national_dex}") from exc
        if slot.species.casefold() != specimen.species.casefold():
            raise ValueError(
                f"Species mismatch for #{specimen.national_dex}: "
                f"expected {slot.species!r}, got {specimen.species!r}"
            )
        slot.specimens.append(specimen)
        slot.hunting = False
        return slot

    def mark_hunting(self, national_dex: int, active: bool = True) -> None:
        self.slots[national_dex].hunting = active

    @property
    def completed_slots(self) -> int:
        return sum(slot.is_complete for slot in self.slots.values())

    @property
    def total_slots(self) -> int:
        return len(self.slots)

    @property
    def completion_ratio(self) -> float:
        return self.completed_slots / self.total_slots if self.total_slots else 0.0

    @property
    def duplicate_count(self) -> int:
        return sum(slot.duplicate_count for slot in self.slots.values())

    def next_missing(self) -> list[LivingDexSlot]:
        return [slot for _, slot in sorted(self.slots.items()) if not slot.is_complete]

    def summary(self) -> dict[str, object]:
        hunting = sum(slot.hunting and not slot.is_complete for slot in self.slots.values())
        return {
            "completed": self.completed_slots,
            "total": self.total_slots,
            "completion_ratio": self.completion_ratio,
            "hunting": hunting,
            "duplicates": self.duplicate_count,
        }
