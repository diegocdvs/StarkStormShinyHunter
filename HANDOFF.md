# StarkStormShinyHunter — AI Handoff

## Purpose
This file is the canonical continuity entry point for another AI agent or developer. No project-critical requirement should exist only in chat history.

## Product goal
Build a modular agent that can autonomously obtain shiny Pokémon across Pokémon Generations I–V using legitimate gameplay progression and generation-specific hunting mechanics, with reproducible emulator automation, safe checkpoints, capture assurance, provenance, save orchestration, and a Shiny Living Dex tracker.

## Current strategy
- Knowledge Base scope: Generations I–V.
- First vertical PoC: Pokémon Emerald + mGBA.
- Expand adapters/mechanics generation-by-generation only after proving the vertical pipeline.
- Fail closed whenever ROM identity, save identity, encounter safety, shiny-lock behavior, or checkpoint determinism is uncertain.

## Non-negotiable invariants
1. Never modify MASTER_SAVE directly. Clone to WORKING_SAVE.
2. Preserve ENCOUNTER_RAW before risky capture operations whenever technically possible.
3. SHINY_SECURED requires successful capture plus validated persisted save/backup.
4. ROM-specific patches require exact identity/hash validation.
5. Unlocked hunts use isolated alternate ROM/save lineage and explicit provenance.
6. Never silently overwrite saves or mix a save with an incompatible ROM/revision.
7. Keep all captured shinies unless an explicit policy says otherwise.
8. ROMs, personal saves, credentials, tokens and webhooks are private assets and must not be committed.

## Core subsystems
- EmulatorAdapter: emulator-neutral control contract; mGBA is first adapter.
- RNG Engine: generation/game-specific RNG and encounter generation models.
- Story Progression Engine: plays campaign prerequisites and stops before critical/irreversible encounter triggers.
- Hunt Route Planner: orders campaign targets and resource preparation to reduce backtracking.
- Capture Assurance: protects rare encounters against flee, self-KO, Roar/Whirlwind, Teleport, Struggle, Safari failure and input errors.
- Save Orchestrator: fingerprints, inventories, clones, selects and switches among saves safely.
- Breeding Pokémon Repository: catalog of donor saves containing breeding parents; trades/transfers a needed parent into the target breeding save using generation-compatible mechanics.
- Shiny Lock Registry / Unlocked Hunt Mode: encounter-level lock knowledge and minimal validated unlock workflows in isolated alternate saves.
- Shiny Living Dex Tracker: HTML dashboard, provenance and automatic update only after SHINY_SECURED.
- Discord integration: alerts/interaction without committing secrets.

## Hunt protocols
### Wild encounters
Validate encounter table/method/resources, preserve encounter state, detect shiny, capture with rollback, persist, update tracker.

### Static / legendary
Use walkthrough-driven story prerequisites and Legendary Access Paths. Stop before irreversible trigger, prepare capture resources, create MASTER_PRE_HUNT_SAVE, hunt, preserve ENCOUNTER_RAW, capture and continue campaign.

### Eggs
Generation-specific checkpoint because shiny/PID determination timing differs. Automate parent setup, egg collection, hatch routing, detection, persistence and box management.

### Masuda
Gen IV onward. Prefer specialized completed saves when available. B2W2 completed saves with Shiny Charm are priority breeding assets where applicable. Validate parent origin languages; maintain reusable foreign-parent library.

### Gen II breeding
Prioritize obtaining a shiny Ditto breeding asset first, then use the generation's DV inheritance mechanics for high-efficiency shiny breeding. Research/implementation must validate the exact 1/64-compatible parent pair rules rather than assuming every pairing qualifies. A Red Gyarados → Gen I → Ditto transformation/trade-back workflow has been requested as an optional bootstrap path and must be independently validated before automation.

### Platinum Poké Radar
Each hunt specification can require species + gender + nature. Keep every shiny, but continue the chain until a shiny matches requested attributes. Validate a safe savestate point before each encounter/patch interaction so restoration does not invalidate chain/RNG state. Use Synchronize where mechanically beneficial and verified.

## Save classes
- MASTER_SAVE: immutable user/base save.
- WORKING_SAVE: operational clone.
- SPECIALIZED_SAVE: breeding, Masuda, Shiny Charm, Cute Charm or other dedicated strategy.
- UNLOCKED_HUNT_SAVE: isolated lineage for shiny-lock removal.

Each save manifest should include game/version/region/language, trainer metadata when safe, progress, Pokédex state, key resources, capabilities, ROM fingerprint compatibility, parent inventory summary, lineage, provenance and checksum/hash.

## Generation notes
- Gen I: no visible native shiny mechanic. Track retroactive shiny-compatible DV provenance where relevant and Gen I↔II transfer workflows.
- Gen II: DV-based shininess, breeding farm, shiny Ditto bootstrap, roamers/static/wild/eggs and transfer interoperability.
- Gen III: RSE/FRLG; Emerald is PoC; LCRNG/save integrity/method-specific generation under active development.
- Gen IV: DPPt/HGSS; breeding, Masuda, Poké Radar (Platinum), Cute Charm-related workflows, Apriball/resource considerations, roamers.
- Gen V: BW/B2W2; separate RNG/Timer0/RTC/emulator validation; B2W2 Shiny Charm specialized saves; shiny locks.

## Living Dex
National Dex scope through #649 for Gen I–V project phase. Track origin game/generation/save, current save, method/subtype, ball, location/date, duplicate count, gender/nature where relevant, lock/unlock provenance and transfer history. Sprites should be locally hosted project assets derived from the selected Pokémon Database sprite source policy; do not hotlink.

## Documentation status convention
- CONFIRMED: supported by authoritative/primary technical evidence.
- PARTIAL: evidence exists but limits/context remain unresolved.
- PENDING: research or experiment required.
- TESTED: reproduced by project code/PoC.

## Private asset boundary
Google Drive/private storage may contain ROMs, saves, walkthroughs and guides. GitHub contains code, schemas, manifests, hashes/fingerprints where appropriate, tests and continuity documentation, never copyrighted ROM binaries or personal save binaries.

## Immediate execution order
1. Keep consolidating requirements into versioned docs/schemas/tests.
2. Complete Gen I–V research matrices and encounter/hunt protocol matrices.
3. Complete Emerald vertical PoC prerequisites: ROM identity gate, save integrity, mGBA adapter, deterministic checkpoints, RNG/encounter observation.
4. Execute Emerald end-to-end only when the exact private ROM/save environment is available.
5. Adversarially validate rollback/capture/save invariants.
6. Generalize interfaces, then add Gen II and DS adapters/mechanics incrementally.

## Handoff rule
Before claiming a milestone complete, ask: “Could a new agent with repository + authorized Drive access continue correctly without chat history?” If not, documentation is incomplete.
