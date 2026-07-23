# Hunt Protocol Matrix v0.1

Status: architecture baseline. Every generation/game-specific claim must be promoted through PENDING → PARTIAL/CONFIRMED → TESTED before autonomous execution.

| Protocol | Gen I | Gen II | Gen III | Gen IV | Gen V | Mandatory safety gate |
|---|---|---|---|---|---|---|
| Wild random encounter | retroactive DV provenance only | yes | yes | yes | yes | encounter table + method + ENCOUNTER_RAW/rollback strategy |
| Static/legendary | retroactive DV cases | yes | yes | yes | yes | story prerequisite map + PRE_HUNT stop + capture readiness |
| Egg/breeding | no native shiny display | DV breeding | standard breeding | standard + Masuda | standard + Masuda + B2W2 Charm where applicable | generation-specific determination checkpoint |
| Gen II Shiny Ditto breeding farm | transfer/bootstrap support | primary | n/a | n/a | n/a | exact DV inheritance compatibility validated; do not assume universal 1/64 |
| Poké Radar targeted chain | n/a | n/a | n/a | Platinum/DPPt-specific validation | n/a | chain-safe checkpoint experimentally TESTED before automation |
| RNG manipulation | game-specific research | game-specific research | Emerald PoC first | game-specific | Timer0/RTC/emulator-specific | exact ROM/save/environment fingerprint |
| Shiny-lock unlocked hunt | n/a conceptually | research per encounter | registry | registry | registry | isolated ROM/save lineage + exact hash + minimal patch + provenance |

## Universal hunt lifecycle

1. Resolve target and requested constraints (species; optional gender/nature/ball/quantity/origin).
2. Select eligible game/method/save through Hunt Route Planner + Save Orchestrator.
3. Validate ROM/save fingerprints and capability manifest.
4. Establish Capture Readiness and required resources.
5. Create protocol-specific pre-hunt checkpoint.
6. Generate encounters/eggs deterministically or iteratively according to the selected method.
7. Detect shiny without mutating the protected raw state.
8. Preserve ENCOUNTER_RAW or equivalent protocol checkpoint whenever technically meaningful.
9. Capture/hatch/secure; rollback on recoverable failure.
10. Validate persisted save and backup before emitting SHINY_SECURED.
11. Record provenance, duplicates, target-attribute match, transfer lineage and Living Dex state.
12. Continue if the hunt specification requires additional specimens or a gender/nature match.

## Protocol-specific invariants

### Wild
- Never assume encounter tables across versions/revisions are identical.
- Model encounter trigger type (walk/surf/fishing/headbutt/swarm/special tiles/etc.).
- Abilities, repel manipulation, time/day and other modifiers are explicit inputs where applicable.

### Static / legendary
- Story Progression must stop before irreversible triggers.
- Legendary Access Path must list flags, badges, HMs/key items, event triggers and missability.
- Roamers require a separate release/generation timing model.

### Eggs
- Never assume shiny is decided at hatch time.
- Track parents, languages, breeding compatibility, egg generation checkpoint, hatch count and box capacity.
- Keep reusable foreign-parent assets indexed in the private Breeding Pokémon Repository.

### Gen II breeding
- Obtain/prepare a shiny-compatible Ditto asset before bulk breeding when that strategy is selected.
- The requested Red Gyarados → Gen I → Ditto bootstrap/glitch path remains PENDING until independently reproduced and documented.
- The often-cited 1/64 result is conditional on compatible DV inheritance; implementation must calculate eligibility rather than attach 1/64 blindly to every offspring.
- Bulk breeding may continue beyond the first shiny to satisfy Living Dex evolution-family needs.

### Poké Radar
- Hunt spec supports required gender and nature; keep all shinies but continue until TARGET_MATCH.
- A savestate before each risky encounter/patch action is allowed only after emulator/game experiments prove restoration preserves chain and intended RNG semantics.
- Record chain length and each captured duplicate separately.

## Evidence rule
No row in this matrix authorizes automation by itself. Generation/game-specific knowledge records and reproducible tests are required before status TESTED.