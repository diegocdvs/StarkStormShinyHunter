# Emerald Legendary Access Paths v0.1

Status: Research artifact — Sprint 0

## Purpose
Define story-progression gates and safe pre-hunt stopping points for Emerald legendary targets. This is an operational input to the future Story Progression Engine and Hunt Route Planner, not a substitute for runtime validation.

## Source hierarchy
1. User Drive walkthroughs/guides for operational route instructions.
2. Decompilation/source-level evidence for event flags and scripts where available.
3. Reputable reference walkthroughs for cross-checking progression order.
4. Emulator experiments before any irreversible automation is marked TESTED.

## Rayquaza
- Story dependency: the weather crisis after Groudon and Kyogre awaken must progress to Sootopolis; Wallace is met in Cave of Origin and the player identifies Sky Pillar.
- First Sky Pillar visit: Rayquaza is awakened as a story event and leaves to stop Groudon/Kyogre. This is **not** the capture attempt.
- After the Sootopolis resolution, Rayquaza returns to Sky Pillar and can be battled/captured before the Elite Four.
- Operational classification:
  - First apex interaction: `STORY_TRIGGER / DO_NOT_HUNT`.
  - Return after crisis resolution: `PRE_HUNT_STOP` before initiating battle.
- Capture risk notes: Lv.70; Rest can remove status/heal; Outrage can lead to confusion/self-damage. Capture Readiness must account for self-KO risk and survivability.
- Ball policy: Luxury Ball if obtainable/stocked in the active game context; otherwise normal Poké Ball per project policy.

## Groudon
- In Emerald, capture is post-Hall-of-Fame, unlike the story awakening event.
- After Elite Four, abnormal weather information leads to Terra Cave on one of the eligible routes.
- Operational classification:
  - Story awakening: `STORY_TRIGGER / NOT CAPTURABLE HERE`.
  - Terra Cave encounter: `PRE_HUNT_STOP` immediately before battle trigger.
- Route/location can change; runtime logic must query/derive the active abnormal-weather location rather than hard-code one route.

## Kyogre
- In Emerald, capture is post-Hall-of-Fame, unlike the story awakening event.
- After Elite Four, abnormal weather information leads to Marine Cave on one of the eligible routes.
- Operational classification:
  - Story awakening: `STORY_TRIGGER / NOT CAPTURABLE HERE`.
  - Marine Cave encounter: `PRE_HUNT_STOP` immediately before battle trigger.
- Route/location can change; runtime logic must query/derive the active abnormal-weather location rather than hard-code one route.

## Regirock / Regice / Registeel
- Unlock chain requires Sealed Chamber puzzle prerequisites, including traversal to Route 134/underwater chamber and party/move prerequisites.
- The trio should be treated as a shared unlock quest followed by three independent static encounters.
- Operational classification:
  - Sealed Chamber completion: `UNLOCK_MILESTONE`.
  - Each individual chamber before battle: `PRE_HUNT_STOP`.
- Exact puzzle actions and party ordering must be reconciled against the user's Drive walkthrough and source scripts before automation is marked CONFIRMED/TESTED.

## Story Progression Engine invariants
1. Never interpret a story appearance of a legendary as a capturable encounter without target-specific confirmation.
2. Before any one-time/static encounter trigger, create `MASTER_PRE_HUNT_SAVE` and verify `CaptureReadiness == PASS`.
3. Do not cross a `PRE_HUNT_STOP` automatically until team, status control, HP control, Ball stock, escape/self-KO risks, PP clock and checkpoint capability pass.
4. At battle generation, create and validate `ENCOUNTER_RAW` before capture actions.
5. Story route and capture route are distinct state-machine phases.
6. Any discrepancy between walkthrough, source scripts and runtime behavior is a hard stop for that target only, not permission to guess.

## Research status
- Rayquaza story/capture separation: CONFIRMED by cross-reference; runtime not yet TESTED.
- Groudon/Kyogre postgame cave capture model: CONFIRMED by cross-reference; dynamic route handling not yet TESTED.
- Regi unlock concept: CONFIRMED at high level; exact automation sequence remains PARTIAL pending source/walkthrough reconciliation.
