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
3. SHINY_FOUND is not SHINY_SECURED. SHINY_SECURED requires successful capture plus validated persisted save/backup.
4. ROM-specific patches require exact identity/hash validation.
5. Unlocked hunts use isolated alternate ROM/save lineage and explicit provenance.
6. Never silently overwrite saves or mix a save with an incompatible ROM/revision.
7. Keep all captured shinies unless an explicit policy says otherwise.
8. ROMs, personal saves, credentials, tokens and webhooks are private assets and must not be committed.
9. Unknown story-trigger or checkpoint safety must fail closed rather than guess.
10. Every milestone requires direct validation plus an adversarial/double-check pass for gaps, contradictions, false positives and edge cases.

## Core subsystems
- EmulatorAdapter: emulator-neutral control contract; mGBA is first adapter.
- RNG Engine: generation/game-specific RNG and encounter generation models.
- Story Progression Engine: plays campaign prerequisites and stops before critical/irreversible encounter triggers.
- Hunt Route Planner: orders campaign targets and resource preparation to reduce backtracking.
- Capture Assurance: protects rare encounters against flee, self-KO, Roar/Whirlwind, Teleport, Struggle, Safari failure and input errors.
- Save Orchestrator: fingerprints, inventories, clones, selects and switches among saves safely.
- Breeding Pokémon Repository: private catalog of donor saves containing breeding parents. When a target parent is absent from the destination breeding save, locate a compatible donor save/game and use a generation-compatible legitimate trade/transfer path. Example: for Bulbasaur breeding in Gen II, obtain Bulbasaur from an indexed compatible donor/Gen I save, capture or select a disposable exchange Pokémon on the destination side, execute the trade, verify the received Bulbasaur, record transfer provenance, then start breeding. Save binaries remain private; Git tracks manifests/schemas only.
- Shiny Lock Registry / Unlocked Hunt Mode: encounter-level lock knowledge and minimal validated unlock workflows in isolated alternate saves.
- Shiny Living Dex Tracker: HTML dashboard, provenance and automatic update only after SHINY_SECURED.
- Discord integration: alerts/interaction without committing secrets.

## Hunt protocols
### Wild encounters
Validate encounter table and method (walking/surf/fishing/etc.), target availability, level distribution, time/day/environmental conditions and generation-specific encounter modifiers. Prepare capture resources, execute encounters, and when a shiny is generated preserve ENCOUNTER_RAW before risky capture actions whenever technically possible. Capture Assurance handles flee/self-KO/forced-switch/Teleport/Struggle/Safari and input risks. Persist only after validated capture/save, then update provenance/tracker/notifications.

### Static / legendary
Use walkthrough-driven story prerequisites and Legendary Access Paths. Story Progression must know badges, flags, HMs/key items, NPC/event triggers, puzzles and irreversible encounter triggers. Stop before the encounter, prepare team/resources, create MASTER_PRE_HUNT_SAVE, generate/hunt, preserve ENCOUNTER_RAW, capture with rollback protection, validate durable save, then continue campaign. Optimize target ordering through Hunt Route Planner rather than treating every legendary as an isolated run.

### Eggs
Do not assume shininess is decided at hatch. Use a generation/game-specific checkpoint at the actual determination point for relevant egg attributes. Automate parent setup, compatibility validation, egg collection, batch/box management, hatch routing, Flame Body/Magma Armor where applicable, shiny detection and durable persistence. Never release/overwrite an unvalidated shiny.

### Masuda
Gen IV onward only. Prefer specialized completed saves when available. B2W2 completed saves with Shiny Charm are priority breeding assets where the target/mechanics benefit. Validate parent origin languages from Pokémon metadata rather than save UI language. Maintain a reusable foreign-parent library, especially Ditto. Preserve immutable complete MASTER_SAVE assets and operate on clones.

### Gen II breeding
Gen II breeding is a first-class/high-volume strategy. Prioritize obtaining a shiny Ditto breeding asset first when feasible, then exploit validated DV inheritance rules for high-efficiency shiny offspring. The commonly cited 1/64 result applies only to compatible breeding configurations; code/docs must model the actual DV/inheritance conditions rather than blindly assigning 1/64 to every pairing. A Red Gyarados → Gen I → Ditto transformation/trade-back glitch workflow has been requested as an optional bootstrap path and must be independently validated from technical evidence and experiment before automation. Breed intensively where useful for Living Dex/evolution-family coverage rather than automatically stopping after the first shiny.

### Breeding Pokémon Repository
Maintain an indexed private donor/parent catalog across compatible saves. If a desired parent is absent from the breeding game (e.g. Bulbasaur needed in Gen II), select a compatible donor save, use a supported trade/transfer path, exchange against a disposable captured Pokémon where appropriate, validate both resulting saves, record provenance, then breed. Prefer real supported game trade/transfer mechanics over direct Pokémon-byte injection when provenance is intended to represent gameplay acquisition.

### Platinum Poké Radar
Each hunt specification supports species plus desired gender and nature (ANY permitted). Keep every legitimate shiny obtained, but continue until at least one shiny matches the requested characteristics. Use Synchronize only where mechanically beneficial and verified. Save-state placement before encounter/patch interaction must be empirically validated: restoring must preserve chain integrity and the assumed RNG/patch state. Do not claim a generic “savestate before every encounter” rule TESTED until this experiment passes. Non-matching shinies remain preserved as duplicates/provenance records.

## Save classes
- MASTER_SAVE: immutable user/base save.
- WORKING_SAVE: operational clone.
- SPECIALIZED_SAVE: breeding, Masuda, Shiny Charm, Cute Charm or other dedicated strategy.
- UNLOCKED_HUNT_SAVE: isolated lineage for shiny-lock removal.

Each save manifest should include game/version/region/language, trainer metadata when safe, progress, Pokédex state, key resources, capabilities, ROM fingerprint compatibility, parent inventory summary, lineage, provenance and checksum/hash.

## Save switching protocol
Target/method selection -> query Save Registry -> select compatible save profile -> verify ROM/save fingerprints -> clone MASTER if needed -> load ROM+working save -> validate expected game/trainer/progress/capabilities -> execute workflow -> validate persisted result -> update inventory/provenance -> switch only after current save is safely closed/backed up. Never infer compatibility from filename alone.

## Breeding repository transfer provenance
Every donor-parent operation must record: target species, donor save identifier, donor game/generation/language, source slot/box when available, destination save identifier, transfer/trade mechanism, disposable exchange Pokémon if used, pre/post fingerprints, validation result, and resulting breeding-parent identity. Never mutate the donor MASTER_SAVE; operate on clones when a transfer changes state.

## Generation notes
- Gen I: no visible native shiny mechanic. Track retroactive shiny-compatible DV provenance where relevant and Gen I↔II transfer workflows.
- Gen II: DV-based shininess, breeding farm, shiny Ditto bootstrap, roamers/static/wild/eggs and transfer interoperability.
- Gen III: RSE/FRLG; Emerald is PoC; LCRNG/save integrity/method-specific generation under active development.
- Gen IV: DPPt/HGSS; breeding, Masuda, Poké Radar (Platinum), Cute Charm-related workflows, Apriball/resource considerations, roamers.
- Gen V: BW/B2W2; separate RNG/Timer0/RTC/emulator validation; B2W2 Shiny Charm specialized saves; shiny locks.

## Shiny locks / alternate save policy
Canonical and unlocked hunts must remain distinct. Workflow: establish encounter-level lock evidence -> identify exact ROM revision/hash -> design minimal unlock -> apply only to alternate copy with hash gate -> use isolated save lineage -> progress normally to original encounter -> hunt/capture normally -> record original hash, patched identity, patch manifest, target, save lineage and result. Never patch an unknown revision or canonical master asset.

## Living Dex
National Dex scope through #649 for Gen I–V project phase. Track origin game/generation/save, current save, method/subtype, Ball, location/date, duplicate count, gender/nature where relevant, lock/unlock provenance and transfer history. Automatic captured state occurs only after SHINY_SECURED. Sprites should be locally hosted project assets consistent with the selected Pokémon Database sprite reference/source policy; do not hotlink.

## Documentation status convention
- CONFIRMED: supported by authoritative/primary technical evidence.
- PARTIAL: evidence exists but limits/context remain unresolved.
- PENDING: research or experiment required.
- TESTED: reproduced by project code/PoC under documented conditions.
Never promote CONFIRMED to TESTED without an actual project experiment.

## Private asset boundary
Google Drive/private storage may contain ROMs, saves, walkthroughs and guides. GitHub contains code, schemas, manifests, hashes/fingerprints where appropriate, tests and continuity documentation, never copyrighted ROM binaries or personal save binaries.

## Immediate execution order
1. Keep README/HANDOFF/project-state documentation synchronized as requirements change.
2. Complete Gen I–V research matrices and encounter/hunt protocol matrices.
3. Complete Emerald vertical PoC prerequisites: ROM identity gate, save integrity, mGBA adapter, deterministic checkpoints, RNG/encounter observation.
4. Build machine-readable Save Registry/Orchestrator and private-asset manifest schemas, including specialized and donor-save inventory.
5. Formalize/validate Gen II shiny Ditto + breeding workflow from technical sources and experiments.
6. Formalize Platinum Poké Radar checkpoint experiment and requested-characteristic schema.
7. Integrate Living Dex transitions with SHINY_SECURED.
8. Execute Emerald end-to-end only when the exact authorized private ROM/save environment is available.
9. Adversarially validate rollback/capture/save invariants.
10. Generalize interfaces, then add Gen II and DS adapters/mechanics incrementally.

## Genuine external blockers
Do not request user input while autonomous research/specification/testing can continue. Likely future blockers are: selecting/authorizing a specific private ROM/save for live emulator testing; access to an emulator/runtime environment; private integration credentials; or a product decision with materially different irreversible behavior.

## Handoff rule
Before claiming a milestone complete, ask: “Could a new agent with repository + authorized Drive access continue correctly without chat history?” If not, documentation is incomplete. A new agent should inventory repository docs/tests/current commits, reconcile this file with project-state/roadmap artifacts, run tests, and continue the highest-priority unblocked item. If documentation conflicts with implementation, stop unsafe execution and resolve from evidence rather than guessing.
