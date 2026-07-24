# StarkStormShinyHunter — Project State

Last consolidated: 2026-07-24

## Phase
Research Sprint 0 / architecture and vertical-PoC preparation.

## Scope
Autonomous shiny-hunting assistance/automation for Pokémon Generations I–V, with Emerald + mGBA as the first end-to-end vertical proof of concept.

## Completed / established
- Master governance: Drive for extensive research/source material; GitHub for code, schemas, tests, concise technical docs and continuity artifacts.
- AI continuity contract in `HANDOFF.md`; README points new agents there first.
- Gen I–V capability matrix baseline.
- Gen I–II DV shiny domain primitives and invariant tests.
- Gen II shiny-Ditto breeding protocol baseline, including explicit validation requirement for the claimed 1/64 offspring path and optional Red Gyarados → Gen I → Ditto bootstrap workflow.
- Breeding Pokémon Repository architecture with donor-save transfer provenance.
- Gen III LCRNG core baseline and deterministic tests.
- EmulatorAdapter contract and initial mGBA bridge direction.
- ROM identity/hash fail-closed primitives and patch hash gates.
- Story Progression Engine / Hunt Route Planner domain design with fail-closed critical-trigger handling.
- Save/checkpoint safety concepts including immutable MASTER_SAVE policy, WORKING_SAVE clones, MASTER_PRE_HUNT_SAVE and ENCOUNTER_RAW.
- Shiny Lock Registry baseline, machine-readable registry direction, ROM hash gate and isolated UNLOCKED_HUNT provenance.
- Shiny Living Dex tracker MVP architecture/schema/tests and HTML UI direction through National Dex #649.
- Sprite policy: local project assets based on selected Pokémon Database generation/game sprite sets; no hotlinking.
- Hunt protocol baselines: wild, static/legendary, eggs, Masuda, Gen II breeding, Platinum Poké Radar.
- Specialized-save model including B2W2 completed saves with Shiny Charm as preferred Masuda/breeding assets where applicable.

## In progress
1. Consolidate all requirements into versioned requirement/protocol documents and machine-readable schemas.
2. Expand Knowledge Base matrices for Gen I–V with status CONFIRMED/PARTIAL/PENDING/TESTED.
3. Emerald vertical PoC prerequisites: exact ROM identity gate; save integrity/fingerprinting; mGBA adapter integration; deterministic checkpoint validation; RNG/encounter observation; Capture Assurance integration.
4. Story-progression extraction from walkthroughs, starting with Emerald legendary access paths.
5. Save Orchestrator and private-asset manifest schemas.
6. Breeding repository inventory schema and legitimate generation-compatible trade/transfer planning.
7. Gen II breeding validation: shiny-parent/Ditto inheritance constraints and exact 1/64-compatible configurations.
8. Platinum Poké Radar validation: safe pre-encounter savestate semantics, chain preservation, requested gender/nature matching.
9. Living Dex provenance, duplicates, transfer history and automatic SHINY_SECURED ingestion.

## Priority backlog
### P0 — safety and reproducibility
- Finish Save Registry schema and fingerprint/lineage validation.
- Define emulator checkpoint determinism test harness.
- Finish Emerald save-integrity and encounter-observation prerequisites.
- Keep unknown ROM/save/trigger states fail-closed.

### P1 — Emerald vertical PoC
- Identify authorized exact Emerald ROM revision by hash.
- Bind symbols/addresses only after identity confirmation.
- Validate mGBA control/read/state primitives in runtime.
- Demonstrate story checkpoint -> encounter -> ENCOUNTER_RAW -> reproducible restore -> capture -> persisted validated save -> SHINY_SECURED -> tracker event.

### P2 — breeding/save orchestration
- Donor-save inventory manifest and parent capability query.
- Gen I↔II legitimate trade workflow for unavailable Gen II parents such as Bulbasaur.
- Gen II shiny Ditto bootstrap and exact DV-based breeding optimization.
- Specialized Platinum/HGSS breeding saves.
- B2W2 completed-save profile with Shiny Charm + Masuda capability.

### P3 — Platinum Poké Radar
- Hunt request schema: species, gender/ANY, nature/ANY and match policy.
- Empirically identify safe savestate point(s) without invalidating chain assumptions.
- Preserve every shiny while continuing until requested gender+nature match.

### P4 — expansion
- Gen II emulator adapter and campaign/hunt automation.
- DS adapter selection/validation for Gen IV/V including RTC/Timer0/savestate determinism.
- Expand story/legendary paths game-by-game.
- Complete encounter-level shiny-lock evidence and validated alternate-save workflows.

## Explicit user requirements captured
- Progress through story autonomously when a target requires campaign advancement.
- Use walkthroughs/guides as operational sources for legendary access, not merely RNG references.
- Apply checkpoint/capture-safety protocol to random encounters as well as static/legendary encounters.
- Egg hunts require generation-specific determination/checkpoint semantics.
- Support Masuda Method using specialized completed saves; prioritize B2W2 Shiny Charm saves where mechanically applicable.
- Gen II breeding should first establish a shiny Ditto/high-value shiny breeding asset and then breed intensively for Living Dex coverage; never assume 1/64 without validating exact inheritance conditions.
- Maintain a private repository/catalog of donor saves containing breedable Pokémon; source unavailable parents via supported trade/transfer, validate both saves, record provenance, then breed.
- Platinum/HGSS breeding saves are supported.
- Platinum Poké Radar hunts accept species, desired gender and desired nature; keep all shinies but continue until target attributes match.
- Validate safe savestates around Poké Radar encounters only after proving chain/RNG restoration behavior.
- Shiny-lock removals use alternate isolated ROM/save lineages, minimal encounter-level patches, exact ROM fingerprint gates and explicit provenance.
- Living Dex tracker is HTML-based, uses locally stored selected Pokémon Database sprites, and records provenance/duplicates/methods.
- All major projects must support model-independent handoff; no project-critical requirement may exist only in chat.

## Explicitly not complete / not TESTED
- No end-to-end live Emerald PoC against the user's exact authorized ROM/save runtime.
- Gen II shiny Ditto/glitch automation is not TESTED.
- Platinum Poké Radar savestate strategy is not TESTED.
- DS emulator determinism assumptions are not TESTED.
- Shiny-lock patches are not safe for arbitrary ROM revisions; exact identity gate remains mandatory.

## Current blockers requiring user/private environment later
None requiring immediate user action.

The first unavoidable private-environment gate is the Emerald end-to-end PoC: exact legitimate ROM/save assets and emulator runtime must be available so the project can fingerprint the ROM/revision and empirically validate memory addresses, RNG observation, savestate determinism and save persistence. Do not request these until preparatory work that can be completed without them is exhausted.

## Next autonomous actions
1. Maintain canonical requirements with stable IDs and traceability.
2. Add/refine protocol schemas for hunt specifications, save manifests, donor-parent inventory and provenance events.
3. Cross-check Gen II breeding claims against primary/decompilation-quality sources before marking CONFIRMED.
4. Continue Emerald PoC implementation/tests that do not require private ROM bytes.
5. Keep `HANDOFF.md`, README and this file synchronized after material changes.

## Completion gate
A milestone is not complete until implementation/research is double-checked adversarially and another agent with repository + authorized Drive access could continue without chat history.
