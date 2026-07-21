# Legendary Access Path Matrix — Sprint 0

Purpose: convert story walkthroughs into machine-actionable access paths while separating navigation evidence from technical RNG/encounter evidence.

## Evidence policy
- Walkthrough/official guide: story order, maps, required progression, key items, navigation.
- Technical/decomp/RNG source: exact generation timing, flags, shiny locks, RNG method.
- Emulator experiment: savestate semantics, memory addresses, deterministic replay.

No target is TESTED until exact-version runtime validation is complete.

## Emerald — initial path model
### Rayquaza
Status: PARTIAL.
Story chain: progress through the Groudon/Kyogre crisis -> Cave of Origin interaction with Wallace -> identify Sky Pillar -> travel to Sky Pillar and awaken Rayquaza as required by story -> resolve Sootopolis crisis -> return to Sky Pillar for the optional capture encounter.
Safety: awakening/story interaction and later capture must be modeled as distinct nodes. Create milestone checkpoints before story-critical Sky Pillar interaction and before later capture approach.
Source basis: user's Drive contains `Detonado Emerald.pdf` and Prima Emerald guide; external walkthrough corroboration indicates Rayquaza returns to Sky Pillar after resolving the Groudon/Kyogre battle.
Open technical checks: exact generation point for capture PID, memory flags, savestate boundary, ROM revision differences.

### Groudon / Kyogre
Status: PENDING/PARTIAL.
Emerald capture access differs from Ruby/Sapphire and is post-story dependent. Build separate paths rather than inheriting R/S logic. Exact weather-institute/event dependencies and generation boundaries remain to be corroborated before automation.

### Regirock / Regice / Registeel
Status: PARTIAL.
Treat Sealed Chamber unlock as a shared prerequisite graph followed by three target-specific branches. Braille/puzzle actions are explicit story nodes. Do not solve from a generic macro: party composition, field moves and exact interaction sequence must be represented as prerequisites.

## FRLG — initial path model
Targets include Articuno, Zapdos, Moltres, Mewtwo and version-dependent roamer. Each receives a separate access path because story gates differ. Roamer release/generation is modeled independently from encounter/capture.
Status: PENDING until walkthrough extraction and technical generation timing are reconciled.

## DPPt — initial path model
Separate Diamond/Pearl from Platinum. Model mascot story encounters, Lake trio, roamers, postgame targets and event-only encounters independently. Do not inherit encounter generation semantics across versions without evidence.
Status: PENDING.

## HGSS — initial path model
Separate HeartGold/SoulSilver mascot requirements and opposite-mascot postgame access. Version mascot access requires story-specific bell/wing progression. Roamers are protected release triggers.
Apricorn preparation is integrated into story routing: acquire Apricorn Box early, collect trees opportunistically, unlock Kurt after Slowpoke Well progression, then schedule crafting before hunt windows.
Status: PARTIAL.

## BW / B2W2 — initial path model
Separate BW from B2W2 entirely. Story mascots, roamers/static encounters, postgame targets, Memory Link-dependent optional content, and shiny-lock rules require independent technical corroboration. Do not infer hardware RNG timing from emulator behavior.
Status: PENDING.

## Machine-readable fields to implement next
`game`, `version`, `target`, `minimum_story_node`, `required_badges`, `required_flags`, `required_key_items`, `required_field_moves`, `resource_preparation`, `generation_trigger`, `pre_hunt_stop`, `irreversible_actions`, `checkpoint_policy`, `capture_policy`, `source_ids`, `evidence_status`.
