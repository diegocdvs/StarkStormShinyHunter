from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class CheckpointKind(str, Enum):
    MASTER_PRE_HUNT = "master_pre_hunt"
    ENCOUNTER_RAW = "encounter_raw"
    CAPTURE_WORKING = "capture_working"
    CAPTURED = "captured"


@dataclass(frozen=True, slots=True)
class Checkpoint:
    kind: CheckpointKind
    path: Path
    sha256: str
    immutable: bool

    def validate(self) -> None:
        if len(self.sha256) != 64:
            raise ValueError("sha256 must be a 64-character hex digest")
        int(self.sha256, 16)
        if self.kind is CheckpointKind.ENCOUNTER_RAW and not self.immutable:
            raise ValueError("ENCOUNTER_RAW must be immutable")
