# Story Progression Engine Contract v0.1

## Purpose
The Story Progression Engine advances a save through the minimum safe campaign path required to unlock each shiny target without accidentally consuming, rerolling, releasing, defeating, or otherwise invalidating a unique encounter.

## Core concepts

### StoryState
- game/version/region/revision
- badges and major progression flags
- key items/HMs and field-move capability
- current map/warp
- party readiness
- money/resources
- unlocked travel routes
- triggered unique encounters

### LegendaryAccessPath
For every legendary or unique target:
- target species and encounter type
- minimum story milestone
- required badges/flags
- required key items/HMs/field moves
- required NPC/event triggers
- ordered route/warp sequence
- one-time/missable/roamer semantics
- PRE_HUNT_STOP trigger boundary
- recommended MASTER_PRE_HUNT_SAVE location
- RNG generation method and shiny-lock status (separate validated registry)
- Capture Readiness requirements

### Trigger safety classification
- SAFE: may be crossed during autonomous progression.
- PRE_HUNT_STOP: agent must stop before crossing until pre-hunt preparation is PASS and a master save exists.
- IRREVERSIBLE: crossing can consume or materially alter a unique encounter; requires explicit policy and recovery plan.

## Invariants
1. Never cross PRE_HUNT_STOP for a target until Capture Readiness = PASS.
2. Never treat walkthrough prose as RNG/shiny-lock authority; cross-validate mechanics separately.
3. Never overwrite the last known-good campaign checkpoint.
4. Persist a milestone save before major story flags and unique encounter releases.
5. For roamers, model the release/generation event separately from the later battle encounter.
6. A walkthrough route must be version-specific; do not assume equivalent flags across paired/sequel games.
7. If emulator input diverges from expected StoryState, stop progression and recover to the last verified milestone rather than improvising blindly.

## Planning algorithm
1. Load target registry and current StoryState.
2. Compute unmet prerequisites for the next target.
3. Choose the shortest safe progression path that does not invalidate later targets.
4. Schedule resource acquisition along the route (capture team, balls, healing, HMs/key items).
5. Save at verified milestones.
6. Stop at PRE_HUNT_STOP.
7. Run Legendary Pre-Hunt Preparation and Capture Readiness.
8. Create MASTER_PRE_HUNT_SAVE.
9. Hand off to RNG/Hunt Engine.
10. After SHINY_SECURED and durable save validation, resume story planning.

## Evidence model
Every route node should record source, page/section when available, game/version applicability, and status: CONFIRMED, PARTIAL, PENDING, or TESTED.

## Initial Emerald validation notes
- The project Drive contains an Emerald walkthrough and a Prima Emerald guide; these are operational route sources.
- External cross-checks confirm Sky Pillar is integrated into the main Emerald story before Rayquaza later becomes an optional capture target.
- Emerald static/legendary targets such as Regirock, Regice, Registeel, Latias/Latios, Kyogre, Groudon and Rayquaza are documented as Method 1 targets in established RNG references; encounter-specific implementation still requires version/emulator validation.

## Test gates
- Route replay reaches expected map/flag state.
- PRE_HUNT_STOP occurs before encounter generation/consumption.
- Reloading campaign milestone reproduces the same pre-trigger state.
- Unique target remains available after route completion.
- No required resource becomes inaccessible due to route optimization.
