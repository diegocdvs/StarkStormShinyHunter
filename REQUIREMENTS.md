# StarkStormShinyHunter — Canonical Requirements

This file assigns stable IDs to project requirements. Detailed mechanics belong in linked protocol/architecture/knowledge-base documents; tests and code should reference these IDs where practical.

## Governance and continuity
- GOV-001 — No project-critical requirement may exist only in chat history.
- GOV-002 — GitHub stores code, tests, schemas, concise technical docs and continuity artifacts; private/copyrighted binaries and secrets are excluded.
- GOV-003 — Extensive research/source material may live in authorized Drive storage, with GitHub retaining enough indexes/manifests/context for handoff.
- GOV-004 — Every material milestone requires adversarial double-check and model-independent handoff readiness.

## Asset identity and safety
- SAFE-001 — Never modify a MASTER_SAVE directly; operate on fingerprinted WORKING_SAVE clones.
- SAFE-002 — Never silently overwrite saves or pair a save with an incompatible ROM/revision.
- SAFE-003 — ROM-specific patches require exact fingerprint/hash validation and fail closed on mismatch.
- SAFE-004 — Preserve ENCOUNTER_RAW before risky capture operations whenever technically possible and empirically safe.
- SAFE-005 — SHINY_SECURED requires capture plus validated persisted save/backup.
- SAFE-006 — Unlocked hunts use isolated alternate ROM/save lineage and explicit provenance.

## Generation scope
- GEN-001 — Knowledge Base and capability planning cover Generations I–V.
- GEN-002 — Gen I is modeled as non-native-visible-shiny gameplay with retroactive DV-compatible provenance/Gen I↔II interoperability where relevant.
- GEN-003 — Gen II uses DV-based shiny/breeding mechanics and requires mechanics-specific validation.
- GEN-004 — Emerald + mGBA is the first vertical PoC before broad multi-generation implementation.
- GEN-005 — DS generations require separate emulator/RNG/RTC/Timer0 validation rather than extrapolation from GBA behavior.

## Story progression and target access
- STORY-001 — Agent can progress campaign prerequisites autonomously to reach hunt targets.
- STORY-002 — Walkthroughs/guides are operational sources for routes, badges, flags, HMs/key items, puzzles and irreversible triggers.
- STORY-003 — Critical encounter triggers are fail-closed and classified so the agent stops before prematurely consuming one-time targets.
- STORY-004 — Hunt Route Planner may order targets/resources to reduce backtracking while preserving encounter safety.

## Hunt protocols
- HUNT-001 — Wild/random encounters use validated encounter tables/methods, preparation, shiny detection, checkpoint/capture safety and persistence.
- HUNT-002 — Static/legendary hunts use story prerequisites, pre-hunt preparation, MASTER_PRE_HUNT_SAVE, ENCOUNTER_RAW where safe, capture assurance and continuation.
- HUNT-003 — Egg hunts use generation/game-specific shiny/PID determination checkpoints; never assume hatching itself determines shininess.
- HUNT-004 — Keep all successfully secured shinies by default, including duplicates generated while pursuing target attributes.

## Breeding
- BREED-001 — Support normal breeding, Masuda where available, generation-specific RNG breeding and applicable Shiny Charm combinations.
- BREED-002 — Specialized completed saves may be selected automatically; B2W2 Shiny Charm saves are preferred breeding/Masuda assets where applicable.
- BREED-003 — Gen II breeding prioritizes establishing a shiny Ditto/high-value shiny breeding asset and intensive breeding for Living Dex/evolution-family coverage.
- BREED-004 — The claimed Gen II 1/64 offspring rate is used only when exact parent/DV/inheritance conditions are independently validated; do not generalize it to every shiny-Ditto pairing.
- BREED-005 — Optional Red Gyarados → Gen I → Ditto bootstrap/glitch workflow must be independently validated before automation.
- BREED-006 — Maintain a private Breeding Pokémon Repository/catalog of donor saves and parent inventory.
- BREED-007 — When a required parent is absent, select a compatible donor save/game and prefer legitimate supported trade/transfer mechanics over direct Pokémon-byte injection when provenance matters.
- BREED-008 — Donor MASTER_SAVE remains immutable; transfer operations use clones and record pre/post fingerprints and provenance.

## Platinum Poké Radar
- RADAR-001 — Hunt specification supports species plus desired gender and nature (ANY allowed explicitly).
- RADAR-002 — Keep every shiny captured during a chain but continue until requested target attributes match.
- RADAR-003 — Use Synchronize only when mechanically beneficial and verified.
- RADAR-004 — A pre-encounter/patch savestate strategy may be automated only after empirical validation that restoration preserves intended chain/RNG semantics and does not create hidden corruption.

## Shiny locks
- LOCK-001 — Maintain encounter-level Shiny Lock Registry with evidence status.
- LOCK-002 — Unlock only the minimum validated lock mechanism for the exact ROM/revision/encounter.
- LOCK-003 — Preserve canonical and unlocked hunt lineages separately and expose provenance in tracker records.
- LOCK-004 — Prefer obtaining locked targets in their own original generation/location/event through normal encounter/capture flow after minimal validated unlock, where technically possible.

## Capture Assurance
- CAP-001 — Model flee, self-KO, Roar/Whirlwind, Teleport, Struggle, Safari failure, PP exhaustion and input-error risks as applicable.
- CAP-002 — Capture Readiness validates team, status/HP control, resources and requested Ball policy before committing to critical hunts.
- CAP-003 — Recovery/rollback behavior must be tested rather than assumed deterministic across emulators/generations.

## Save orchestration and transfer
- SAVE-001 — Save Orchestrator fingerprints, inventories, clones, selects and switches saves/ROM contexts safely.
- SAVE-002 — Save manifests record game/version/region/language, safe trainer metadata, progress/capabilities, Pokédex/resources, ROM compatibility, lineage and hashes.
- SAVE-003 — Track origin_save separately from current_save after transfers.
- SAVE-004 — Transfer Planner records generation-compatible movement/trade path and provenance.

## Living Dex tracker
- DEX-001 — HTML Shiny Living Dex dashboard covers National Dex #001–649 for Gen I–V phase.
- DEX-002 — Record status, origin/current save, game/generation, method/subtype, Ball, location/date, duplicates, gender/nature where relevant, lock provenance and transfer history.
- DEX-003 — Automatic captured status occurs only after SHINY_SECURED.
- DEX-004 — Use locally hosted selected Pokémon Database sprite assets; do not hotlink.
- DEX-005 — Tracker supports filters/search/import/export and a versioned data schema.

## Integrations
- INT-001 — Discord can emit hunt/shiny/capture events without committing webhook/token secrets.
- INT-002 — Emulator adapters expose a generation-neutral control boundary; emulator-specific assumptions remain behind adapters.

## Traceability status
Requirement status uses CONFIRMED / PARTIAL / PENDING / TESTED where evidence/mechanics are involved. A requirement being accepted does not imply its underlying mechanical assumptions are CONFIRMED; protocol documents must distinguish product intent from empirical fact.
