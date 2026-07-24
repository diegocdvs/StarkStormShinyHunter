# Gen II Shiny Ditto Breeding Bootstrap — Research Baseline v0.1

## Purpose
Define the evidence-backed baseline for using Shiny Ditto as a high-efficiency breeding asset in Generation II and for optionally bootstrapping that Ditto through the Generation I Transform DV manipulation glitch.

## Status convention
- CONFIRMED: supported by technical/reference evidence.
- PARTIAL: evidence supports the mechanism but project-specific limits remain.
- PENDING: requires further research or emulator experiment.
- TESTED: reproduced by StarkStormShinyHunter under documented conditions.

## Findings

### GEN2-SD-001 — Shininess is DV-based
Status: CONFIRMED.

In Generation II, shininess is determined by DVs. A shiny requires Defense, Speed and Special DVs of 10, with Attack DV in the shiny-compatible set 2, 3, 6, 7, 10, 11, 14 or 15. Because these values persist across Gen I/II trading, a Pokémon with compatible DVs can be non-visibly shiny in Gen I and display as shiny after transfer to Gen II.

Operational implication: Gen I assets may be evaluated for retroactive shiny compatibility, and Gen I↔II transfer provenance must preserve DVs.

### GEN2-SD-002 — Shiny Ditto breeding can yield 1/64 shiny offspring under compatible conditions
Status: CONFIRMED, with constraint.

Generation II breeding partially inherits Defense and Special DVs. When Ditto is a parent, Ditto is the DV-inheriting parent. With a Shiny Ditto, the inherited/random DV conditions can produce a 1/64 shiny probability for compatible offspring. This is not a universal unconditional 1/64 rule for every breeding request; compatibility, species/gender/breeding rules and DV inheritance constraints must be checked.

Operational policy: before a Gen II breeding batch starts, the planner must prove `shiny_ditto_1_64_eligible = true`; otherwise it must calculate/use the correct alternative strategy rather than advertise 1/64.

### GEN2-SD-003 — Shiny Ditto glitch via Gen I is technically documented
Status: CONFIRMED mechanism; PENDING project experiment.

The Transform DV manipulation glitch in Generations I/II allows a wild Ditto that uses Transform twice in the same battle to retain copied DVs. A documented Shiny Ditto workflow uses a shiny-DV Pokémon transferred to Gen I, enables the wild Ditto to copy Transform and transform twice, then catches that Ditto. In Gen I the result has no native shiny display, but after transfer to Gen II its retained DVs make it shiny.

A canonical bootstrap candidate is the story-mandated Red Gyarados from Gen II because it is guaranteed shiny and therefore provides shiny-compatible DVs. A practical Gen I workflow may use Mimic to allow the player's transferred shiny-DV Pokémon to copy Ditto's Transform, after which the wild Ditto can use Transform twice and retain the shiny DVs.

Operational implication: this is an optional `GEN2_SHINY_DITTO_BOOTSTRAP` workflow, not direct save editing.

## Proposed automated workflow
1. Progress Gen II until Red Gyarados is legitimately captured, unless a validated Shiny Ditto asset already exists in the Save/Breeding Repository.
2. Preserve the canonical Gen II MASTER_SAVE; operate on a WORKING_SAVE.
3. Validate a supported Gen I↔II trade environment and exact save/ROM pairing.
4. Transfer the shiny-DV source Pokémon to a compatible Gen I working save.
5. Ensure the source Pokémon has the required move/setup for the selected validated glitch route (e.g. Mimic-based route where applicable).
6. Locate a wild Ditto encounter in Gen I.
7. Create a checkpoint before executing the Transform sequence.
8. Execute the exact Transform-twice sequence.
9. Catch Ditto.
10. Validate caught Ditto identity/DVs before and after transfer back to Gen II.
11. Confirm shiny display/status in Gen II.
12. Persist as a reusable `BREEDING_ASSET: SHINY_DITTO`, with immutable source backup and provenance.
13. Use clones/working saves for breeding operations; never mutate the only master copy.

## Save Repository integration
The Shiny Ditto asset should be indexed by:
- asset_id
- species = Ditto
- shiny = true
- game/generation currently stored in
- source workflow (`NATIVE_HUNT`, `GEN1_TRANSFORM_DV_GLITCH`, other validated method)
- original source Pokémon and source save lineage
- DVs
- language/region/version
- compatible destination saves
- ROM/save fingerprints
- validation status
- backup locations (private; never commit binaries)

The planner should query this asset before starting any Gen II breeding hunt. If absent, bootstrap Shiny Ditto first when feasible and economically preferable.

## Required experiments before TESTED
- Reproduce Gen I Transform-twice DV retention in the selected emulator stack.
- Verify save-state placement does not alter the expected Transform/DV outcome.
- Verify trade round-trip preserves DVs and save integrity.
- Confirm the resulting Ditto is shiny after returning to Gen II.
- Run a controlled breeding sample and inspect inherited DVs against the disassembly/mechanics model.
- Validate which requested offspring are actually eligible for the 1/64 configuration.

## Sources
- pret/pokecrystal disassembly: https://github.com/pret/pokecrystal
- Bulbapedia, Shiny Pokémon / Generation II DV determination and breeding probability: https://bulbapedia.bulbagarden.net/wiki/Shiny_Pok%C3%A9mon
- Bulbapedia, Pokémon breeding / Generation II shiny breeding: https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_breeding
- Bulbapedia, Transform glitches / Shiny Ditto glitch: https://bulbapedia.bulbagarden.net/wiki/Shiny_ditto_glitch

## Safety / provenance rule
Never label a result `TESTED` solely because a video or community guide demonstrates it. External demonstrations establish research evidence; StarkStormShinyHunter must reproduce the workflow under an identified ROM/save/emulator configuration before automation is considered validated.