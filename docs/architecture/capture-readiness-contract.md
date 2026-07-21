# Capture Readiness Contract v0.1

## Purpose
No critical hunt may start merely because the target is reachable. The system must prove that the current save, team, resources and recovery strategy can safely sustain the encounter and capture attempt.

## Mandatory gate
`Capture Readiness = PASS` is required before legendary, roamer, Safari, one-time and other explicitly critical encounters.

The gate fails closed when any required fact is unknown.

## Required dimensions

1. **Team survivability** — estimate worst credible incoming damage, recovery capacity, resistances/immunities and expected number of capture turns. Unknown movesets or mechanics remain blockers until bounded.
2. **HP control** — a verified way to reduce HP without unintended KO, accounting for immunity, recoil, weather, contact abilities and generation-specific mechanics.
3. **Status control** — paralysis or sleep selected per target/mechanics. Status choice is target-specific, not a universal hard-coded preference.
4. **Ball stock** — enough eligible balls for the policy and target risk envelope. Running out during an encounter is not considered an acceptable normal strategy.
5. **Checkpoint safety** — MASTER_PRE_HUNT_SAVE exists and the encounter-specific ENCOUNTER_RAW semantics have been experimentally validated for that emulator/game/context before rollback is trusted.
6. **Escape/self-KO hazards** — Roar/Whirlwind/Teleport, flee mechanics, Explosion/Self-Destruct, recoil, Perish Song, Struggle and equivalent mechanics must be identified and mitigated or explicitly blocked.
7. **PP exhaustion** — maintain a conservative turn/PP budget. The engine must not wait until Struggle is reached to react.

## Ball policy
Precedence:
1. Ball forced by game mechanics (for example Safari Ball).
2. HGSS: preserve the encounter, then request the user's Apriball choice from available stock.
3. Other games: Luxury Ball when available in the applicable context; otherwise standard Poké Ball.

Capture probability never silently overrides the user's ball policy. Instead, preparation and rollback strategy must be adapted. If the requested policy cannot be executed safely, readiness fails.

## Checkpoint invariant
`ENCOUNTER_RAW` is immutable after creation. A separate `CAPTURE_WORKING` state may be replaced during attempts. Reload equivalence must be demonstrated experimentally; a savestate is not assumed to preserve identical encounter semantics across all games/emulators.

## Output
The readiness report exposes a deterministic list of blockers. Orchestration must call `require_pass()` before a critical hunt transition. Any unmitigated risk prevents progression.

## Next implementation increments
- generation-aware damage/survivability adapter;
- target moveset/risk registry;
- PP exhaustion clock;
- ball-stock estimator with conservative confidence margin;
- status/HP-control compatibility rules;
- integration with Story Progression Engine and Hunt Route Planner.
