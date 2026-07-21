# Gen V Shiny Lock Registry v0.1

Status vocabulary: CONFIRMED / PARTIAL / PENDING / TESTED.

## Confirmed baseline

| Target | Game/context | Lock status | Proposed profile | Notes |
|---|---|---:|---|---|
| Victini | Black/White, static encounter | CONFIRMED | UNLOCKED_HUNT | Wild/static encounter is prevented from being shiny. Japanese BW has a distinct failure behavior when a shiny-generating value occurs; international behavior differs, so patches must be revision/language-specific. |
| Reshiram | Black/White story capture | CONFIRMED | UNLOCKED_HUNT | Story-critical encounter cannot be shiny. Preserve story progression and capture semantics when removing only the shiny restriction. |
| Zekrom | Black/White story capture | CONFIRMED | UNLOCKED_HUNT | Story-critical encounter cannot be shiny. Preserve story progression and capture semantics when removing only the shiny restriction. |
| Zoroark | Black/White Lostlorn Forest encounter | CONFIRMED | UNLOCKED_HUNT if this exact encounter is desired | This specific encounter is prevented from being shiny; species itself can be obtained shiny by other means, so Living Dex routing should distinguish canonical species completion from origin-specific hunt goals. |

## B2W2 caution

Reshiram/Zekrom are encountered postgame through N/Dragonspiral Tower flows in B2W2. Their exact shiny-lock implementation and revision-specific patch points remain PENDING until verified against game code/ROM revision. Do not inherit BW patch assumptions.

## Design implications

1. Lock registry keys must include game, language/region, revision/hash, encounter identity, and target species.
2. `UNLOCKED_HUNT` must never mutate the canonical save/ROM lineage.
3. Patch scope must be minimal: remove only the shiny-prevention mechanism unless a separate experimental mode explicitly says otherwise.
4. Story-critical encounters require Story Progression Engine integration and a `PRE_HUNT_STOP` before irreversible triggers.
5. Tracker provenance must distinguish `CANONICAL` from `UNLOCKED_HUNT`; a species obtainable shiny canonically elsewhere must not be globally labeled locked.
6. No patch is `TESTED` until encounter generation, save-state rollback, capture, save integrity, and post-capture story progression all pass.

## Source evidence

- Bulbapedia Shiny Pokémon documentation: Gen V introduced prevention for specific wild/static encounters; lists Victini (BW), Reshiram, Zekrom and Lostlorn Forest Zoroark.
- Bulbapedia Black/White documentation: Victini is shiny-locked and Japanese versions exhibit a distinct behavior when a shiny-generating value occurs, fixed in international versions.
- Bulbapedia in-game event Pokémon documentation: BW Reshiram/Zekrom story captures cannot be shiny.

## Next research gates

- Locate exact lock routines in decomp/disassembly or verified binary research for each BW/B2W2 revision.
- Build hash-keyed patch manifests rather than universal offsets.
- Validate whether B2W2 Reshiram/Zekrom use the same conceptual lock but different implementation.
- Map event/gift locks separately from wild/static locks.
- Add automated regression tests ensuring patch manifests refuse unknown ROM hashes.
