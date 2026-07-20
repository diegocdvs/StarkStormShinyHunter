# Sprint 0 — Source Registry

Status vocabulary: `CONFIRMED`, `PARTIAL`, `PENDING`, `TESTED`.

## Emulator layer

### mGBA scripting API — CONFIRMED
Primary source: official mGBA scripting documentation.

Capabilities relevant to the project:
- read/write emulator memory;
- read/write registers;
- save/load savestates from files, slots or buffers;
- get/set pressed buttons;
- reset emulation;
- frame and instruction stepping;
- screenshots;
- callbacks including frame, reset, crash and save-data updates;
- ROM checksum and game metadata.

Important limitation to validate for cloud execution:
- official historical scripting notes explicitly listed true headless execution as absent; current deployment architecture must therefore be benchmarked rather than assumed.

## Generation III

### Pokémon Emerald — CONFIRMED BASE SOURCE
Primary reverse-engineering source: `pret/pokeemerald` decompilation.

Reference ROM identity exposed by the project:
- Pokémon Emerald SHA-1: `f3ae088181bf583e55daf962a92bb46f4f1d07b7`.

Research tracks:
- RNG implementation and seeding;
- Pokémon creation methods by encounter type;
- save-block structures and checksums;
- party/box Pokémon structures;
- wild/static/gift/egg/Safari behavior;
- battle/capture edge cases.

### FireRed / LeafGreen — CONFIRMED BASE SOURCE
Primary reverse-engineering source: `pret/pokefirered`.

The project distinguishes multiple English revisions with distinct SHA-1 values. Version/revision must therefore be part of every technical profile; memory addresses and patches must never be assumed portable across revisions without validation.

## Generation IV

Primary reverse-engineering repositories to use as first-tier technical sources:
- `pret/pokeplatinum`;
- `pret/pokeheartgold`.

Status: PARTIAL until the exact RNG, save, encounter and capture structures required by our automation are mapped and cross-tested.

## Generation V

Games in scope:
- Black;
- White;
- Black 2;
- White 2.

Required research dimensions:
- initial seed derivation and boot-time timing inputs;
- Timer0 variability;
- RNG streams used for IVs/PID/encounters and their interaction;
- RTC/date/time behavior;
- emulator determinism vs retail-hardware guides;
- wild/static/gift/egg/roamer/special encounters;
- shiny locks;
- Shiny Charm behavior in B2W2;
- save structure, TID/SID/PID and legality relationships;
- savestate reproducibility and restore semantics.

Critical caution: retail hardware RNG guides are not automatically valid for emulators. Any claim that depends on hardware timing, Timer0, RTC or boot entropy remains `PENDING` until reproduced on the selected DS emulator.

## Source hierarchy

1. Official emulator documentation and source code.
2. Matching decompilation/disassembly/source-level reverse-engineering projects.
3. Maintained open-source RNG tools where algorithms can be inspected.
4. High-quality written community guides for operational procedure.
5. Video demonstrations as reproducibility evidence, not sole specification.

## Validation rule

A critical mechanic may move from `PENDING`/`PARTIAL` to `CONFIRMED` only when its source is identified and its scope is explicit. It moves to `TESTED` only after our own reproducible test passes for the exact game, version/region, emulator and configuration in use.
