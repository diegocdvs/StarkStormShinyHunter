# StarkStormShinyHunter — Project State

Last consolidated: 2026-07-22

## Phase
Research Sprint 0 / architecture and vertical-PoC preparation.

## Scope
Autonomous shiny-hunting assistance/automation for Pokémon Generations I–V, with Emerald + mGBA as the first end-to-end vertical proof of concept.

## Completed / established
- Master governance: Drive for extensive research/source material; GitHub for code, schemas, tests, concise technical docs and continuity artifacts.
- AI continuity contract in `HANDOFF.md`.
- Gen I–V capability matrix baseline.
- Gen I–II DV shiny domain primitives and invariant tests.
- Gen II shiny-Ditto breeding protocol baseline, including explicit validation requirement for the claimed 1/64 offspring path and optional Red Gyarados → Gen I → Ditto bootstrap workflow.
- Breeding Pokémon Repository architecture with donor-save transfer provenance.
- Gen III LCRNG core baseline and deterministic tests.
- EmulatorAdapter contract and initial mGBA bridge direction.
- Story Progression Engine / Hunt Route Planner domain design with fail-closed critical-trigger handling.
- Save/checkpoint safety concepts including immutable MASTER_SAVE policy, WORKING_SAVE clones, MASTER_PRE_HUNT_SAVE and ENCOUNTER_RAW.
- Shiny Lock Registry baseline, machine-readable registry direction, ROM hash gate and isolated UNLOCKED_HUNT provenance.
- Shiny Living Dex tracker MVP architecture/schema/tests and HTML UI direction through National Dex #649.
- Sprite policy: local project assets based on selected Pokémon Database generation/game sprite sets; no hotlinking.
- Hunt protocol baselines: wild, static/legendary, eggs, Masuda, Gen II breeding, Platinum Poké Radar.
- Specialized-save model including B2W2 completed saves with Shiny Charm as preferred Masuda/breeding assets where applicable.

## In progress
1. Consolidate all conversational requirements into versioned requirement/protocol documents and machine-readable schemas.
2. Expand Knowledge Base matrices for Gen I–V with status CONFIRMED/PARTIAL/PENDING/TESTED.
3. Emerald vertical PoC prerequisites:
   - exact ROM identity gate;
   - save integrity and fingerprinting;
   - mGBA adapter integration;
   - deterministic savestate/checkpoint validation;
   - RNG/encounter observation;
   - Capture Assurance integration.
4. Story-progression extraction from walkthroughs, starting with Emerald legendary access paths.
5. Save Orchestrator and private-asset manifest schemas.
6. Breeding repository inventory schema and legitimate generation-compatible trade/transfer planning.
7. Gen II breeding mechanics validation, including shiny-parent/Ditto inheritance constraints and exact 1/64 conditions.
8. Platinum Poké Radar protocol validation, especially safe pre-encounter savestate semantics and chain preservation.
9. Living Dex tracker provenance model, duplicate handling, target gender/nature tracking and automatic SHINY_SECURED ingestion.

## Explicit user requirements captured
- Progress through story autonomously when a target requires campaign advancement.
- Use walkthroughs/guides as operational sources for legendary access, not merely RNG references.
- Apply checkpoint/capture-safety protocol to random encounters as well as static/legendary encounters.
- Egg hunts require generation-specific determination/checkpoint semantics.
- Support Masuda Method using specialized completed saves; prioritize B2W2 Shiny Charm saves where mechanically applicable.
- Gen II breeding should first establish a shiny Ditto/high-value shiny breeding asset and then breed intensively for Living Dex coverage; never assume 1/64 without validating the exact compatible inheritance conditions.
- Maintain a private repository/catalog of donor saves containing breedable Pokémon; e.g. source Bulbasaur from a compatible donor/Gen I save, perform a legitimate trade using a disposable destination Pokémon, validate transfer, then breed in Gen II.
- Platinum/HGSS breeding saves are supported.
- Platinum Poké Radar hunts accept species, desired gender and desired nature; keep all shinies but continue until target attributes match.
- Validate and use safe savestates around Poké Radar encounters only after proving chain/RNG restoration behavior.
- Shiny-lock removals use alternate isolated ROM/save lineages, minimal encounter-level patches, exact ROM fingerprint gates and explicit provenance.
- Living Dex tracker is HTML-based, visually polished, uses locally stored selected Pokémon Database sprites, and records provenance/duplicates/methods.
- All major projects must support model-independent handoff; no project-critical requirement may exist only in chat.

## Current blockers requiring user/private environment later
None requiring immediate user action.

The first unavoidable private-environment gate is the Emerald end-to-end PoC: exact legitimate ROM/save assets and emulator runtime must be available so the project can fingerprint the ROM/revision and empirically validate memory addresses, RNG observation, savestate determinism and save persistence. Do not request these until all preparatory work that can be completed without them is exhausted.

## Next autonomous actions
1. Create/maintain canonical `REQUIREMENTS.md` with stable requirement IDs and traceability.
2. Add protocol schemas for hunt specifications, save manifests, donor-parent inventory and provenance events.
3. Cross-check Gen II breeding claims against primary/decompilation-quality sources before marking CONFIRMED.
4. Continue Emerald PoC implementation and tests that do not require private ROM bytes.
5. Keep `HANDOFF.md` and this file synchronized after material architectural or requirement changes.

## Completion gate
A milestone is not complete until implementation/research is double-checked adversarially and another agent with repository + authorized Drive access could continue without chat history.
