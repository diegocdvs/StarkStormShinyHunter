# Story Progression Engine — v0.1

The agent must progress each game campaign before accessing targets that are gated by story progression.

For each target, the knowledge base records the game/version, minimum story milestone, badges and event prerequisites, key items and field moves, route to the encounter, encounter class, one-time or missable behavior, recommended pre-hunt save location, shiny eligibility, and capture-readiness requirements.

Progression steps are classified as SAFE, PRE_HUNT_STOP, or CRITICAL_TRIGGER. Before a critical target, the agent stops, validates capture readiness, creates a permanent backup and a master pre-hunt save, and only then activates the hunt workflow.

The Hunt Route Planner may reorder optional targets to reduce backtracking and prepare capture resources in advance, but it must never consume a one-time encounter during generic story automation.

Walkthroughs and strategy guides in the private Drive are operational navigation sources. Claims affecting RNG, shiny eligibility, encounter generation, or save safety require technical cross-validation or experiment before being marked CONFIRMED or TESTED.

Emerald research already confirms that ordinary wild encounters and many stationary/event targets use different generation methods. Therefore encounter-generation logic must remain target/context specific rather than universal.
