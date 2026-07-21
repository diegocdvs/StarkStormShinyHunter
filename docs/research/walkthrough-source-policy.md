# Walkthrough Source Policy

Walkthroughs already stored in the project's private Drive are first-class operational sources for story navigation and legendary access sequencing.

## Known corpus
The Drive corpus includes walkthroughs/guides for Emerald, FireRed/LeafGreen, Diamond/Pearl, Platinum, HeartGold/SoulSilver, Black/White and Black 2/White 2, plus official/Prima-era guides for several generations.

## Evidence boundaries
Walkthroughs may establish:
- route/order of story progression
- NPC/event sequence
- badges, HMs, key items and access prerequisites
- dungeon/puzzle navigation
- practical point at which a legendary becomes reachable

Walkthroughs alone do **not** establish:
- RNG internals or frame behavior
- exact Pokémon generation timing
- shiny-lock implementation
- emulator savestate determinism
- memory addresses

Those claims require technical corroboration and/or project testing.

## Legendary extraction schema
For each legendary/roamer/event target extract:
- target/game/version
- earliest safe story access
- mandatory prerequisites
- exact trigger boundary
- missable/one-time/roamer classification
- `SAFE`, `PRE_HUNT_STOP`, `IRREVERSIBLE` markers
- recommended `MASTER_PRE_HUNT_SAVE` location
- continuation route after successful capture
- walkthrough citation + technical corroboration status

## Anti-gap rule
A route is not automation-ready until both navigation and trigger semantics are known. Unknown trigger semantics force a stop before the suspected trigger.
