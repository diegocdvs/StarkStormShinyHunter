# Gen I–II Shiny Knowledge Base v0.1

Status vocabulary: CONFIRMED / PARTIAL / PENDING / TESTED.

## Generation I — Red / Blue / Yellow

### Model

Generation I has no native visible Shiny state. For project purposes, a Pokémon obtained in Gen I can be classified as `RETROACTIVE_SHINY_CANDIDATE` only when its DVs satisfy the Generation II shiny predicate and the intended provenance path preserves those DVs into Gen II.

### Confirmed mechanics

- Gen II shiny predicate: Defense=10, Speed=10, Special=10, Attack in {2,3,6,7,10,11,14,15}.
- A Gen I Pokémon with those DVs becomes visibly Shiny when traded into Gen II.
- Due to Gen I PRNG correlations, ordinary grass/cave/Surf encounters cannot produce the Gen-II-shiny DV combination. Fishing, gifts, stationary encounters and in-game trades can span all DV combinations and can therefore yield retroactive shiny candidates.

### Project policy

- Never label a Gen I specimen `SHINY_SECURED` while it exists only in Gen I; use `RETROACTIVE_SHINY_CANDIDATE`.
- Promote to `SHINY_SECURED` only after deterministic DV verification plus successful transfer/trade into Gen II and visible/structural shiny verification.
- Record acquisition class (`FISHING`, `GIFT`, `STATIC`, `INGAME_TRADE`, etc.) because eligibility differs by encounter generator.
- Gen I wild grass/cave/Surf routes are fail-closed for retroactive shiny hunting unless a specific game/version exception is independently demonstrated.

## Generation II — Gold / Silver / Crystal

### Confirmed mechanics

- Shininess is DV-based with the predicate above.
- Baseline random-DV shiny probability is 1/8192.
- Breeding can reach 1/64 under the relevant inheritance relationship from a shiny parent; eligibility must be evaluated from inherited Defense/Special DVs rather than assuming every pairing can produce a shiny.
- The Lake of Rage red Gyarados is a forced story shiny encounter.
- Crystal Odd Egg has elevated shiny probability that varies by language/version; this must be represented as version-specific encounter metadata rather than a universal rate.
- Roamer DVs and HP are initialized on first encounter and persist; this makes the pre-initialization story/event boundary a critical checkpoint.
- Only Unown I and V can satisfy the shiny + form constraints in native Gen II mechanics.

### Required engine additions

1. `Gen2DVShinyPredicate` — exact DV predicate and tests.
2. `Gen1RetroactiveEligibility` — encounter-class gate plus DV verification.
3. `Gen2BreedingPlanner` — inheritance-aware shiny feasibility and probability.
4. `Gen2RoamerCheckpointPolicy` — checkpoint before DV initialization.
5. `Gen2SpecialEncounterRegistry` — Red Gyarados, Odd Egg and version/language-specific cases.
6. GB/GBC emulator adapter research — deterministic memory/input/save-state semantics before automation.

## Living Dex provenance extensions

Add acquisition modes:

- `RETROACTIVE_SHINY` — acquired in Gen I, verified shiny after Gen II transfer.
- `CANONICAL` — native shiny mechanics.
- `UNLOCKED_HUNT` — encounter-level shiny lock/restriction deliberately removed in isolated alternate environment.
- `RNG_OPTIMIZED` — RNG manipulation without removing an encounter lock.
- `CUTE_CHARM` — Gen IV Cute Charm-specific profile.

Required Gen I retroactive evidence fields:

- source game/version/language
- encounter class
- source save identity
- DVs before transfer
- transfer/trade path
- destination Gen II save identity
- shiny verification result

## Double-check / unresolved

- Do not conflate original cartridge Time Capsule behavior with Virtual Console Poké Transporter behavior; they are distinct provenance paths.
- Poké Transporter historical versions had differing conversion behavior; transporter version must be recorded if that route is ever supported.
- Exact Gen I encounter-generator restrictions must be validated per game/version before automated target routing.
- Exact Odd Egg probabilities must be stored by language/version and independently sourced before implementation.
- Mew/event distributions require event-specific provenance; do not infer eligibility from species alone.

## Sources

Research baseline consulted: Bulbapedia pages on Shiny Pokémon, DVs/IVs, breeding, roaming Pokémon, Poké Transporter, transfer mechanics, and unobtainable Shiny Pokémon. Critical implementation facts must be cross-validated against disassembly/decompilation or direct emulator tests before status `TESTED`.
