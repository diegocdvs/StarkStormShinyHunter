# Shiny Lock Registry — Gen III–V

Status: Sprint 0 research registry. Conservative by design: uncertain claims remain `PENDING`/`PARTIAL` until code-level or experimental validation.

## Classification
- `CONFIRMED`: strong technical/documentary evidence.
- `PARTIAL`: broad claim supported, exact mechanism/version scope incomplete.
- `PENDING`: insufficiently demonstrated.
- `TESTED`: reproduced by StarkStormShinyHunter against identified ROM/revision.

## Core modeling rule

`SHINY_LOCKED_ENCOUNTER != SHINY_UNOBTAINABLE_SPECIES`.

Locks are modeled at encounter granularity. A species can be locked in one scripted encounter but obtainable shiny elsewhere. The Living Dex planner should prefer a canonical same-generation method when one exists; `UNLOCKED_HUNT` exists for the explicit goal of hunting a normally locked encounter in its original generation/game context.

## Gen III — R/S/E/FR/LG

Working rule: do **not** assume modern-style forced non-shiny locks for ordinary stationary legendary encounters. Every static, gift, roamer and event target still requires per-version verification. Event distributions are audited separately because distribution PID constraints can differ from in-world encounter logic.

Emerald code baseline: `pret/pokeemerald`; the project documents the reference ROM SHA-1 as `f3ae088181bf583e55daf962a92bb46f4f1d07b7`.

Status: `PARTIAL`, pending exhaustive target-by-target registry and empirical tests.

## Gen IV — D/P/Pt/HGSS

Target-by-target registry remains `PENDING`. Priority: gifts, event distributions, roamers and special scripted encounters. Cute Charm and RNG-optimized saves are separate modes and must not be conflated with shiny-lock removal.

No `UNLOCKED_HUNT` patch is authorized by a generic generation-level assumption.

## Gen V

Generation V introduced explicit anti-shiny behavior for specific in-game encounters. Documentary cross-check identifies Victini, Reshiram, Zekrom and the Lostlorn Forest Zoroark in Black/White as encounters prevented from being shiny. Exact routine/version mapping remains required before patching.

### Black / White

- Victini: `CONFIRMED` documentary encounter lock; mechanism/patch location `PENDING`.
- Reshiram: `CONFIRMED` documentary encounter lock; mechanism/patch location `PENDING`.
- Zekrom: `CONFIRMED` documentary encounter lock; mechanism/patch location `PENDING`.
- Lostlorn Forest Zoroark: `CONFIRMED` documentary encounter lock. This is encounter-specific; shiny Zorua/Zoroark availability through other methods must be modeled separately.

### Black 2 / White 2

- Reshiram/Zekrom static encounters: `CONFIRMED` at documentary level as unable to be shiny; mechanism/patch location `PENDING`.
- Kyurem and every other special encounter: classify independently; never infer lock status from mascot dragons.
- Shiny Charm does not imply explicit shiny locks are bypassed.
- Nature Preserve Shiny Haxorus and Benga's Shiny Gible/Dratini are scripted shiny cases and must not be generalized to other encounters.

## Unlock policy

For every locked target:
1. Identify exact game, region, revision and ROM hash.
2. Demonstrate the lock mechanism at code/data level.
3. Create a separate `UNLOCKED_HUNT` profile; never modify canonical save/ROM silently.
4. Apply the smallest possible patch that removes only forced non-shiny behavior.
5. Preserve species, encounter location, level, moveset, story trigger, base shiny odds and normal capture flow wherever technically possible.
6. Record original/patched hashes and a patch manifest.
7. Run negative-control testing on the unmodified build and positive testing on the patched build.
8. Progress the alternate save through the normal story to the original encounter.
9. Require Capture Readiness PASS and immutable pre-hunt checkpoint.
10. Mark tracker provenance `UNLOCKED_HUNT` only after real capture + valid save + backup.

## Alternate-save naming

`<GAME>_<REGION>_<REV>_diego_UNL_<TARGET>_<NN>.sav`

Canonical and unlocked saves must never share the same mutable working path.

## Patch manifest required fields

- game / region / revision;
- original ROM hash;
- patched ROM hash;
- target species and encounter ID;
- lock mechanism classification;
- exact code/data locations changed;
- semantic description of change;
- expected unaffected behavior;
- validation evidence;
- compatible save lineage;
- rollback/recovery procedure.

## Research priorities

1. BW: map exact anti-shiny implementation for Victini/Reshiram/Zekrom/Zoroark.
2. B2W2: map Reshiram/Zekrom routines and independently classify Kyurem/special encounters.
3. Gen IV: exhaustive static/gift/event registry.
4. Gen III: exhaustive static/gift/event verification against decomps.
5. Add automated ROM hash/revision gate before any unlock patch can execute.
6. Extend tracker schema with `hunt_profile`, `lock_status`, `patch_manifest_id`, `canonical_alternative`.

## Evidence notes

- `pret/pokeemerald` provides an exact Emerald decompilation baseline for code-level verification.
- Bulbapedia's Shiny Pokémon documentation is used as a secondary registry seed for Gen V lock candidates, not as sole authorization for binary patching.
- Story access and lock behavior are separate dimensions: Story Progression Engine must reach the original encounter normally in `UNLOCKED_HUNT` mode.

No ROM binaries, personal saves, copyrighted ROM-byte patches, or credentials are stored in GitHub.
