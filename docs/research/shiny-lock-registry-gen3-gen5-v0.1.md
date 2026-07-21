# Shiny Lock Registry — Gen III–V v0.1

Status vocabulary: CONFIRMED / PARTIAL / PENDING / TESTED.

## Purpose
Track encounters that cannot naturally generate shiny in the exact original game/version and define the evidence and minimum-change strategy required for alternate `UNLOCKED_HUNT` profiles. No ROM binary, save, or copyrighted game asset is versioned here.

## Gen III

### Ruby / Sapphire / Emerald
- Baseline registry status: PENDING exhaustive audit.
- Current engineering assumption: do not classify any target as locked until encounter-specific code/script evidence is reconciled against the exact ROM revision.
- Emerald US decompilation baseline SHA-1: `f3ae088181bf583e55daf962a92bb46f4f1d07b7` (pret/pokeemerald).

### FireRed / LeafGreen
- Baseline registry status: PENDING exhaustive audit by ROM revision.
- Revision identity is mandatory before memory addresses or patches are considered valid.

## Gen IV

### Diamond / Pearl / Platinum
- Status: PENDING exhaustive audit.
- Required evidence: decomp/disassembly or reproducible encounter-generation analysis per target.

### HeartGold / SoulSilver
- Status: PENDING exhaustive audit.
- Special interaction: alternate profiles for Cute Charm RNG must remain distinct from `UNLOCKED_HUNT` profiles.

## Gen V

### Black / White
- Victini — PARTIAL: widely documented as forced non-shiny; mechanism and exact patch point still require code-level confirmation before implementation.
- Reshiram / Zekrom story encounter — PARTIAL: documented as unable to be shiny; exact version-specific mechanism requires code-level confirmation.
- Other static/gift/event targets — PENDING exhaustive audit.

### Black 2 / White 2
- N's Reshiram / Zekrom at Dragonspiral Tower — CONFIRMED at encounter-behavior level: documented as coded never to be shiny. Patch mechanism remains PENDING code-level verification.
- Other static/gift/event targets, including encounter-specific Kyurem behavior — PENDING exhaustive audit; no inheritance of lock status by association.

## Unlock policy
A target may enter `UNLOCKED_HUNT` only when all gates pass:
1. Exact game, language/region and revision identified.
2. Lock existence supported by at least one strong technical source and preferably a second independent source.
3. Lock mechanism identified (forced non-shiny PID, reroll, fixed PID, script behavior, event distribution, etc.).
4. Minimum-change patch designed to remove only the lock.
5. Before/after ROM hashes recorded privately with the run metadata.
6. Regression test confirms species, level, location, encounter flow and capture remain otherwise unchanged.
7. Save is isolated from canonical profile and labeled `UNLOCKED_HUNT`.
8. Tracker records provenance and never represents the result as a canonical unmodified-game shiny.

## Negative-evidence rule
Absence from this registry does **not** mean a Pokémon is huntable. Unknowns are `PENDING`, and the agent must fail closed before investing a long hunt or triggering a one-time encounter.

## Sources / evidence policy
- Prefer decompilation/disassembly and direct encounter-generation code.
- Use walkthrough/database sources to establish encounter behavior and story access, but not as sole authority for patch offsets.
- Emulator experiments can promote a claim to TESTED only for the exact ROM hash and emulator build tested.

## Next research queue
1. Complete BW/B2W2 lock table target-by-target.
2. Audit Gen IV static/gift/event generation using pret decompilation projects where available.
3. Audit Gen III one-time/static/event encounters and explicitly document whether locks exist.
4. Produce per-target patch specifications only after mechanism confirmation.
