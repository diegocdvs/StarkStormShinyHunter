# Save Orchestrator Selection Policy

Status: DESIGN

## Objective
Select the safest and most efficient ROM/save/method combination for each hunt without modifying immutable source saves.

## Selection order
For every target, evaluate:
1. target legality/availability in Gen I-V and desired origin constraints;
2. canonical encounter, static/legendary, breeding, Masuda, Poké Radar, RNG or unlocked-hunt alternatives;
3. registered saves with required story flags, Pokédex, Shiny Charm, parents/donors and resources;
4. expected time/cost and operational risk;
5. Living Dex requirements, including number of specimens needed for evolutionary families;
6. user-specified constraints such as nature/gender for Poké Radar.

## Save classes
- MASTER_SAVE: immutable source artifact; never executed as writable.
- WORKING_SAVE: disposable/rollback-capable clone for normal operations.
- SPECIALIZED_SAVE: prepared for breeding, Masuda, Shiny Charm, Poké Radar, Cute Charm or other specialized workflows.
- UNLOCKED_HUNT_SAVE: isolated clone paired with a validated ROM patch for a specific shiny-locked encounter.
- DONOR_SAVE: source of Pokémon needed as parents or transfer assets; trades occur from a working clone.

## Mandatory matching
A save may be loaded only when ROM identity, game/version/region, save fingerprint and emulator adapter compatibility all match registry metadata. Unknown or ambiguous identity fails closed.

## Breeding donor resolution
When a required parent is absent:
1. search Breeding Donor Registry;
2. choose a compatible donor save and create a working clone;
3. acquire a low-value/random trade counterpart in the destination save when required;
4. execute an in-game trade through the supported generation link mechanism;
5. verify both post-trade saves and Pokémon fingerprints;
6. register transfer provenance;
7. start breeding only after validation passes.

Example: Bulbasaur required for Gen II breeding may be sourced from a registered Gen I donor save, traded legitimately into a Gen II working save in exchange for a disposable captured Pokémon, then used as a parent.

## Gen II preference
For Gen II mass breeding, prefer a registered verified shiny Ditto donor. If unavailable, bootstrap one according to `gen2-shiny-ditto-breeding-protocol.md` before starting the target queue when this materially improves total expected hunt time.

## Gen IV Poké Radar
For Platinum Radar hunts, the hunt specification includes species and explicit gender/nature constraints (ANY allowed). Preserve all shinies, but continue the chain until a shiny satisfying the requested target constraints is secured. Save-state boundaries must be experimentally validated before being used to protect chains.

## Gen V breeding
Prefer registered B2W2 specialized saves with Shiny Charm for compatible breeding workflows, including Masuda where foreign-language parents are available and mechanics permit the combined benefit.

## Audit trail
Every selection emits a plan record containing target, selected game, ROM ID, save ID/class, method, donor dependencies, checkpoint policy, expected success criteria and fallback strategy.
