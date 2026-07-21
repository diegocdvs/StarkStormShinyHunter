# Shiny Lock Registry — Generation V v0.1

Status vocabulary: `CONFIRMED`, `PARTIAL`, `PENDING`, `TESTED`.

This registry is deliberately conservative. `CONFIRMED` means the lock is supported by multiple reputable references or explicit encounter documentation. Patch offsets/implementation details remain `PENDING` until exact ROM revision/hash research and emulator validation are complete.

## Pokémon Black / White

| Target | Encounter | Lock status | Evidence status | Unlocked-hunt requirement |
|---|---|---|---|---|
| Reshiram | N's Castle; Dragonspiral fallback under special full-storage condition | Shiny locked | CONFIRMED | Alternate `UNLOCKED_HUNT` profile required to obtain shiny in Gen V encounter |
| Zekrom | N's Castle; Dragonspiral fallback under special full-storage condition | Shiny locked | CONFIRMED | Alternate `UNLOCKED_HUNT` profile required |
| Victini | Liberty Garden event encounter | Shiny locked | CONFIRMED | Alternate `UNLOCKED_HUNT` profile required; event-access prerequisites must be preserved |
| Kyurem | Giant Chasm | Research required before classification | PENDING | Do not patch or hunt as unlocked until lock mechanism is verified for exact version/revision |

## Pokémon Black 2 / White 2

| Target | Encounter | Lock status | Evidence status | Unlocked-hunt requirement |
|---|---|---|---|---|
| Zekrom (Black 2) | N's Castle sequence → Dark Stone → Dragonspiral Tower | Shiny locked | CONFIRMED | Alternate `UNLOCKED_HUNT` profile required |
| Reshiram (White 2) | N's Castle sequence → Light Stone → Dragonspiral Tower | Shiny locked | CONFIRMED | Alternate `UNLOCKED_HUNT` profile required |
| Kyurem | Giant Chasm after obtaining/capturing version dragon | Research required before final classification | PENDING | Exact lock behavior and patch strategy must be proven before use |
| N's Pokémon | Special encounters | Fixed attributes / special generation; shininess behavior requires per-target research | PARTIAL | Separate from generic shiny-lock removal; do not apply universal patch |

## Operational invariants

1. Never apply a generic 'force shiny' cheat as the production unlock strategy.
2. Identify ROM game, language, region/revision and cryptographic hash before patch selection.
3. Patch only the lock mechanism needed for the target; do not globally alter shiny odds or unrelated encounter generation.
4. Keep canonical and unlocked saves/ROM profiles isolated.
5. Record provenance: original hash, patched hash, patch ID/version, target, save profile and validation evidence.
6. Story Progression Engine must follow the original access path and stop before irreversible encounter triggers.
7. Capture Readiness must pass before triggering the target.
8. `SHINY_SECURED` requires actual capture + valid save + backup verification.
9. Living Dex provenance must record `UNLOCKED_HUNT`; never mislabel as canonical.
10. Any unknown or contradictory behavior fails closed as `PENDING`.

## Confirmed access-path notes

### BW Reshiram / Zekrom
The version mascot is encountered at the climax in N's Castle and is normally mandatory for story progression. Encounter documentation also records a Dragonspiral Tower fallback when capture at N's Castle is prevented by a full party and completely full storage. This edge case must be modeled separately; it must not be used accidentally by autonomous progression.

### B2W2 Zekrom / Reshiram
Post-game progression requires following N's Zoroark to N's Castle, defeating N, receiving the Dark Stone (Black 2) or Light Stone (White 2), and taking it to Dragonspiral Tower. The version dragon is then encountered at level 70. Story flags and the Japanese-version Frozen Zoroark glitch must be accounted for in region-specific routing.

### Victini
Liberty Garden Victini is an in-game encounter gated by event access. The encounter is documented as unable to be shiny. Any unlocked-hunt route must preserve event/story access separately from removal of the shiny-prevention mechanism.

## Research backlog

- Verify Kyurem shiny-lock behavior separately in BW and B2W2 using code-level or reproducible emulator evidence.
- Enumerate all Gen V fixed/gift/event encounters with shiny prevention or fixed PID behavior.
- Locate exact lock mechanism(s) per ROM revision/language.
- Build minimal binary patches only after hashes and offsets are confirmed.
- Test patch isolation: target can be shiny while unrelated shiny odds/generation remain unchanged.
- Validate save-state determinism around each encounter trigger.
- Add automated regression vectors for canonical vs unlocked behavior.

## Sources used for v0.1

- Bulbapedia in-game event encounter documentation for Black/White (Reshiram/Zekrom cannot be shiny; story/fallback behavior).
- Project Pokémon preserved encounter records for Dragonspiral Tower Reshiram/Zekrom in Gen V.
- Project Pokémon preserved Liberty Garden Victini encounter record (PID cannot be shiny).
- Bulbapedia B2W2 walkthrough/access-path documentation.

Web findings are evidence inputs, not patch instructions. Exact patch implementation remains blocked behind ROM identity/revision validation.
