# Emerald Legendary Access Pilot — v0.1

Status: research/specification; not yet TESTED in target ROM/emulator.

## Goal
Use story progression as an explicit prerequisite to legendary hunting. Rayquaza is the first pilot because Emerald separates a mandatory story sequence involving Rayquaza from the later optional capturable static encounter at Sky Pillar.

## Evidence-backed route boundary
1. Progress through the Hoenn campaign until the Groudon/Kyogre crisis in Sootopolis.
2. In Cave of Origin, Wallace asks about the third super-ancient Pokémon; identifying Sky Pillar advances the story toward Rayquaza.
3. Reach Sky Pillar and complete the story sequence that resolves the crisis.
4. After the Groudon/Kyogre conflict is resolved, Rayquaza returns to Sky Pillar and the later visit is an optional route to the capturable encounter.
5. The automation must distinguish these phases and must not treat the story-resolution interaction as the final capture hunt.

## Safety model
- Story approach to the crisis: SAFE/CHECKPOINT depending on chapter.
- Actions that alter the Rayquaza story state: IRREVERSIBLE until exact flag semantics are mapped and tested.
- Later approach to capturable Rayquaza: PRE_HUNT_STOP before the generation trigger.
- Before target interaction: Capture Readiness PASS, required ball inventory, capture team, persistent save backup, and MASTER_PRE_HUNT_SAVE.

## RNG classification
Current research classifies stationary Pokémon in Emerald under Method 1 for practical RNG targeting. Wild encounters use a different generation path and commonly exhibit H-2/Wild-2 behavior; therefore the RNG engine must not reuse the stationary generator for wild targets.

## Research tasks before TESTED
- Map exact story flags and trigger boundaries from decompilation/symbols for the supported Emerald revision.
- Ingest the user's private Emerald walkthrough for operational navigation and compare it with technical sources.
- Verify exact point at which the capturable Rayquaza is generated.
- Verify save-state restoration semantics around the generation trigger.
- Build target-specific capture readiness: level/moveset, dangerous moves, PP clock, tank requirements, status plan, Luxury Ball inventory.
- Verify post-capture story continuation and persistent save integrity.

## Source notes
Operational walkthrough sources and technical RNG sources are tracked separately. Walkthrough material determines navigation/story order; technical sources determine generation semantics and RNG classification.
