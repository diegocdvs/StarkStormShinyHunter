"""Fail-closed ROM identity and patch-manifest primitives."""

from dataclasses import dataclass
from hashlib import sha1
from pathlib import Path


@dataclass(frozen=True)
class RomIdentity:
    game: str
    region: str
    revision: str
    sha1: str


@dataclass(frozen=True)
class PatchManifest:
    manifest_id: str
    expected_rom: RomIdentity
    target: str
    purpose: str

    def validate_bytes(self, rom_bytes: bytes) -> None:
        actual = sha1(rom_bytes).hexdigest()
        if actual.lower() != self.expected_rom.sha1.lower():
            raise ValueError(
                f"ROM hash mismatch for {self.manifest_id}: "
                f"expected {self.expected_rom.sha1}, got {actual}"
            )

    def validate_file(self, path: str | Path) -> None:
        self.validate_bytes(Path(path).read_bytes())


def sha1_bytes(data: bytes) -> str:
    return sha1(data).hexdigest()
