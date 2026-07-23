# Gen II Shiny Ditto Breeding Validation v0.1

## Purpose
Validate the product requirement that Generation II breeding should establish a Shiny Ditto first and then use it as a high-efficiency breeding parent, including the commonly cited 1/64 shiny offspring probability.

## Evidence status

### CONFIRMED — shininess is DV-based
In Generation II, a Pokémon is shiny when Defense, Speed and Special DVs are 10 and Attack DV is one of 2,3,6,7,10,11,14,15. This makes shiny status inheritable indirectly through breeding DV mechanics.

### CONFIRMED — 1/64 is conditional, not universal
Generation II breeding passes Defense and Special-related DVs from one parent; when Ditto is used, Ditto is the inheriting parent source. With a compatible shiny-DV parent source, the remaining random conditions yield 1/64 shiny offspring: inherited Defense is 10; inherited Special has a 1/2 path to 10; random Attack has 1/2 probability of a shiny-compatible value; random Speed has 1/16 probability of 10. Product logic MUST therefore gate the 1/64 label on validated parent/DV compatibility rather than treating every breeding pair as 1/64.

### CONFIRMED — two shiny Pokémon cannot breed normally in Gen II
The breeding compatibility rule rejects parents with the same Defense DV and matching Special-DV relationship; consequently two ordinary shiny parents cannot breed with each other. The Shiny Ditto strategy pairs Shiny Ditto with a non-shiny compatible target parent/species, not Shiny Ditto + another shiny.

### CONFIRMED — Shiny Ditto glitch exists across Gen I/II interoperability
A wild Ditto that uses Transform twice after copying shiny-compatible DVs can permanently retain those DVs and become a Shiny Ditto. A Generation I execution path can use a shiny Pokémon transferred from Gen II (notably the story-guaranteed Red Gyarados as the accessible shiny seed), exploit Transform/DV behavior against wild Ditto, catch it, and trade it back to Gen II. Exact operational steps, game/version constraints, emulator link/trade behavior and checkpoint safety still require TESTED status before automation.

## Required automation protocol
1. Check Save Registry for an already validated Shiny Ditto asset compatible with the destination Gen II save.
2. If absent, prefer creating/acquiring one through a validated bootstrap workflow rather than beginning bulk breeding without it.
3. Preserve MASTER_SAVE; clone all involved Gen I/II saves before transfers or glitch execution.
4. If using Red Gyarados bootstrap: progress/copy to a state where Red Gyarados is secured; transfer through supported Gen I↔II trade workflow; execute the exact validated Shiny Ditto glitch; verify resulting Ditto DVs/shiny state after return to Gen II.
5. Register Shiny Ditto as a SPECIALIZED breeding asset with provenance and fingerprints.
6. For each breedable Living Dex target, validate species compatibility and DV inheritance eligibility before labeling expected odds 1/64.
7. Breed in batches, preserve every secured shiny, and continue until enough individuals exist for required Living Dex/evolution-family coverage.
8. Record egg counts, parent identities, DVs where observable, save lineage and resulting shiny provenance.

## Fail-closed rules
- Never assume 1/64 solely because one parent is Shiny Ditto.
- Never mutate donor MASTER_SAVE directly.
- Never automate the Transform glitch until exact sequence and emulator trade/state semantics are reproduced in tests.
- Never direct-inject a Shiny Ditto into a save when provenance-preserving gameplay/trade is the selected project mode.

## Sources / validation trail
- pret/pokecrystal disassembly: primary implementation reference for breeding/DV mechanics.
- Bulbapedia Shiny Pokémon / Individual values: secondary mechanics synthesis used to cross-check the 1/64 derivation.
- Bulbapedia Transform glitches / Shiny Ditto glitch: secondary documentation of the Gen I/II Transform DV manipulation workflow.
- User-supplied video reference is retained as an operational lead, not sufficient alone for CONFIRMED mechanics.

## Remaining TESTED gates
- Exact emulator pair/link configuration for Gen I↔II trades.
- Savestate safety before/after link trades.
- Exact Red Gyarados → Gen I → Shiny Ditto → Gen II sequence on the selected ROM revisions.
- Automated DV verification and breeding compatibility gate.
- Batch breeding loop and box-capacity management.
