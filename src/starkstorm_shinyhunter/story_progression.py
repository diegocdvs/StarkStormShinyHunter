"""Compatibility facade for story progression primitives.

Canonical implementation lives in :mod:`starkstorm_shinyhunter.story.progression`.
New code should import from the canonical module; this facade prevents two
independent story-safety models from diverging.
"""

from starkstorm_shinyhunter.story.progression import (
    LegendaryAccessPath,
    StoryRequirement,
    StoryState,
    TriggerClass,
    may_cross_trigger,
)

__all__ = [
    "LegendaryAccessPath",
    "StoryRequirement",
    "StoryState",
    "TriggerClass",
    "may_cross_trigger",
]
