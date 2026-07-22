# Generation I–II Knowledge Base Scope

## Purpose

Extend StarkStormShinyHunter coverage to Generations I and II without incorrectly projecting later-generation shiny mechanics backward.

## Generation I — Red / Blue / Yellow

Generation I has no native visible shiny state. The project therefore treats Gen I as a provenance and transfer-compatibility domain rather than conventional shiny hunting.

### Required research
- DV generation and encounter-generation behavior by game/version.
- Which Gen I Pokémon can become shiny after transfer/trade into Gen II under DV-based shininess rules.
- Static, gift, in-game trade, wild and special encounter constraints.
- Save structure, checksum/integrity and emulator behavior.
- Story progression and legendary access paths.
- Transfer/trade path into Gen II and preservation of identity/provenance.

### Tracker classification
Use `RETROACTIVE_SHINY` only when a Pokémon originating in Gen I satisfies the exact Gen II shiny DV criteria and the result is validated after transfer/trade. Never label a Gen I encounter itself as visibly shiny.

## Generation II — Gold / Silver / Crystal

Generation II is a first-class shiny-hunting domain.

### Required research
- DV-based shiny determination and exact constraints.
- Wild/static/gift/egg/roamer/special encounter generation.
- Breeding mechanics relevant to shiny probability.
- Odd Egg differences where applicable.
- Red Gyarados as guaranteed shiny and tracker classification.
- Save structure, checksum/integrity and RTC implications.
- Story progression, legendary access paths and irreversible triggers.
- Emulator adapter requirements for GB/GBC.
- Capture Readiness adapted to Gen II battle/capture mechanics.

## Safety and evidence rules

Every critical claim is tagged `CONFIRMED`, `PARTIAL`, `PENDING`, or `TESTED`. Version/region differences must be explicit. No later-generation PID/TID/SID model may be reused for Gen I/II. No ROM/save is committed to GitHub.

## Architecture implications

The common pipeline remains Story Progression -> Hunt Route Planner -> Capture Readiness -> checkpoint -> hunt -> capture/validation -> SHINY_SECURED -> tracker, but generation-specific adapters own RNG, shiny determination, save integrity, battle/capture rules and emulator integration.
