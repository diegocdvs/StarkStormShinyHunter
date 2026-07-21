# Story Progression Engine — Contract v0.1

## Purpose
Drive each supported game from a valid save/new game state to hunt-ready checkpoints without accidentally consuming one-time encounters or invalidating RNG/capture prerequisites.

## Core model
A story route is a directed graph of `StoryNode`s. Each node records prerequisites, actions, resulting flags, resources gained/consumed, irreversible effects, and encounter triggers.

### Node safety classes
- `SAFE`: ordinary progression; no protected encounter is consumed.
- `PRE_HUNT_STOP`: progression must stop before executing the trigger until Capture Readiness and hunt preparation pass.
- `IRREVERSIBLE`: action changes a one-time/event/roamer state and requires an explicit validated checkpoint before execution.

## Required node fields
- game/version/region/revision
- node_id and human-readable objective
- prerequisite flags/badges/items/HMs
- navigation/action sequence
- expected postconditions
- protected encounter(s), if any
- safety class
- recommended checkpoint type
- source references and evidence status

## Invariants
1. Never cross `PRE_HUNT_STOP` for a protected target unless `CaptureReadiness == PASS`.
2. Never execute `IRREVERSIBLE` without a validated persistent save backup.
3. Story logic must be version-aware; routes are not assumed portable between paired/remake versions.
4. Roamer release/generation timing is modeled separately from later physical encounter.
5. Walkthroughs guide navigation/progression, while technical claims (RNG, locks, generation timing) require technical corroboration.
6. The engine must verify expected postconditions after each critical node; mismatch halts autonomous progression.

## Legendary access path
Each protected target receives a `LegendaryAccessPath`:
`target -> minimum story state -> required flags/badges/items/HMs -> event/NPC trigger -> navigation -> pre-hunt stop -> Capture Readiness -> MASTER_PRE_HUNT_SAVE -> generation trigger -> ENCOUNTER_RAW -> capture -> persistent save/backup`.

## Recovery
Maintain milestone saves before major chapters and protected triggers. A failed postcondition restores the most recent validated milestone rather than improvising forward.
