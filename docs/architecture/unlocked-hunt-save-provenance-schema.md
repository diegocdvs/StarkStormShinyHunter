# Unlocked Hunt — Save & Patch Provenance Schema v0.1

Every alternate shiny-lock-removal hunt must produce a machine-readable provenance record. This prevents canonical saves from being confused with modified hunt environments.

```json
{
  "profile_type": "UNLOCKED_HUNT",
  "trainer": {"name": "diego", "gender": "male"},
  "game": "Pokemon White 2",
  "generation": 5,
  "rom": {
    "region": null,
    "language": null,
    "revision": null,
    "sha256_original": null,
    "sha256_patched": null
  },
  "unlock": {
    "target_species": "Reshiram",
    "lock_registry_id": null,
    "patch_id": null,
    "patch_version": null,
    "scope": "target-only",
    "validation_status": "PENDING"
  },
  "save": {
    "parent_profile": "CANONICAL",
    "parent_hash": null,
    "derived_hash": null,
    "story_checkpoint": null,
    "backup_verified": false
  },
  "hunt": {
    "encounter_location": null,
    "capture_ball": null,
    "shiny_secured": false,
    "capture_save_hash": null
  }
}
```

## Required gates

- Exact ROM identity before patch.
- Patch registry entry with evidence and target scope.
- Original and patched hashes differ as expected and are recorded.
- Canonical source remains immutable.
- Story checkpoint is reproducible.
- Patch-isolation regression test passes.
- Capture save integrity passes before Living Dex update.

Unknown fields are not guessed. A record with missing critical identity fields remains `PENDING` and cannot be promoted to production hunt status.
