# Hunt Route Planner — Contract v0.1

## Goal
Optimize campaign progression across shiny targets while preserving encounter eligibility and minimizing backtracking/resource preparation.

## Inputs
- target registry and priority
- story graph
- version-specific encounter eligibility and shiny-lock registry
- capture-team readiness
- ball availability policy
- money/items/HMs/key items
- Apricorn/Apriball inventory for HGSS
- travel/backtracking cost
- RNG-method prerequisites

## Constraints
1. Protected one-time encounters cannot be consumed during ordinary story traversal.
2. Shiny-locked targets are never scheduled as normal shiny hunts; modified/unlocked modes are separate explicit profiles.
3. Safari encounters use mandatory Safari mechanics.
4. HGSS protected encounters pause after preservation for Apriball choice where applicable.
5. Other games prefer Luxury Ball, falling back to standard Poké Ball only when Luxury Ball is unavailable under project policy.
6. A critical hunt is schedulable only when Capture Readiness can reach PASS before its generation trigger.

## Output
An ordered `HuntPlan` containing story milestones, preparation tasks, resource farms, target access paths, pre-hunt stops, checkpoints and post-capture continuation nodes.

## Optimization priorities
Safety > encounter eligibility > deterministic reproducibility > capture readiness > resource sufficiency > reduced backtracking/time.

## Validation
Every generated plan is replay-checked against prerequisites/postconditions before execution. Any unresolved version-specific claim blocks only the affected route, not unrelated validated routes.
