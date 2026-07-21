# Shiny Lock Registry — Gen III–V

Status: Sprint 0 research registry. This file is intentionally conservative: uncertain claims remain PENDING/PARTIAL until code-level or experimental validation.

## Classification
- `CONFIRMED`: supported by strong technical/documentary evidence.
- `PARTIAL`: evidence supports the broad claim, but exact mechanism/version scope still needs validation.
- `PENDING`: not yet sufficiently demonstrated.
- `TESTED`: reproduced by StarkStormShinyHunter against identified ROM/revision.

## Gen III

### Ruby / Sapphire / Emerald / FireRed / LeafGreen
Current working rule: do **not** assume modern-style forced non-shiny locks for ordinary stationary legendary encounters. Each event/gift/static target still requires per-version verification before automation. Emerald is the first code-level baseline using `pret/pokeemerald` and exact ROM identity.

Status: `PARTIAL` pending exhaustive target-by-target registry and empirical tests.

## Gen IV

### Diamond / Pearl / Platinum / HeartGold / SoulSilver
Target-by-target registry remains `PENDING`. Particular attention is required for gifts, event distributions, roamers and special scripted encounters. Cute Charm and RNG-optimized saves are separate modes and must not be conflated with shiny-lock removal.

## Gen V

### Black / White
Known special/legendary encounters require explicit lock classification before hunt planning. Reshiram/Zekrom/Victini and event/gift cases are priority research targets. No unlock patch may be generated until exact ROM revision and lock mechanism are demonstrated.

Status: `PARTIAL/PENDING` by target.

### Black 2 / White 2
Reshiram/Zekrom static encounters are documented as unable to be Shiny in the original games. They therefore require `UNLOCKED_HUNT` if the project goal is to capture them shiny in their own Gen V environment. Kyurem and other special encounters must be classified independently rather than inferred from the mascot dragons.

Status for B2W2 Reshiram/Zekrom lock: `CONFIRMED` at documentary level; mechanism/patch location remains `PENDING` until ROM/code analysis.

## Unlock policy

For every locked target:
1. Identify exact game, region, revision and ROM hash.
2. Demonstrate the lock mechanism at code/data level.
3. Create a separate `UNLOCKED_HUNT` profile; never modify the canonical save/ROM silently.
4. Apply the smallest possible patch that removes only the forced non-shiny behavior.
5. Preserve species, encounter location, level, moveset, story trigger and normal capture flow wherever technically possible.
6. Validate before/after hashes and run a regression test showing the encounter remains functional.
7. Progress the alternate save through the normal story to the original encounter.
8. Require Capture Readiness PASS and immutable pre-hunt checkpoint.
9. Mark tracker provenance `UNLOCKED_HUNT` after real capture + valid save + backup.

## Alternate-save naming

`<GAME>_<REGION>_<REV>_diego_UNL_<TARGET>_<NN>.sav`

Canonical and unlocked saves must never share the same mutable working path.

## Research priorities
1. BW: Reshiram, Zekrom, Victini — exact lock implementation and version differences.
2. B2W2: Reshiram/Zekrom — exact lock implementation; Kyurem independent classification.
3. Gen IV: exhaustive special/static/gift/event registry.
4. Gen III: exhaustive static/gift/event verification against decompilations.

## Evidence notes
- `pret/pokeemerald` provides an exact Emerald decompilation baseline and reference SHA-1 for code-level verification.
- B2W2 in-game encounter documentation explicitly identifies Reshiram/Zekrom as unable to be Shiny.
- Story access and lock behavior are separate dimensions: the Story Progression Engine must still reach the original encounter normally in `UNLOCKED_HUNT` mode.

No ROM binaries, personal saves, patches derived from copyrighted ROM bytes, or credentials are stored in GitHub.
