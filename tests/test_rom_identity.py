import hashlib

import pytest

from starkstorm_shinyhunter.rom_identity import PatchManifest, RomIdentity, sha1_bytes


def test_sha1_bytes_is_deterministic():
    data = b"starkstorm-test-rom"
    assert sha1_bytes(data) == hashlib.sha1(data).hexdigest()


def test_patch_manifest_accepts_exact_hash():
    data = b"known-rom-revision"
    identity = RomIdentity("Test", "US", "1.0", hashlib.sha1(data).hexdigest())
    manifest = PatchManifest("test-lock", identity, "Target", "remove shiny lock")
    manifest.validate_bytes(data)


def test_patch_manifest_rejects_unknown_or_wrong_rom():
    expected = b"known-rom-revision"
    identity = RomIdentity("Test", "US", "1.0", hashlib.sha1(expected).hexdigest())
    manifest = PatchManifest("test-lock", identity, "Target", "remove shiny lock")
    with pytest.raises(ValueError, match="ROM hash mismatch"):
        manifest.validate_bytes(b"different-revision")
