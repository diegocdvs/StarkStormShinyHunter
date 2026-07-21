# Generation V — Verified/Pending Findings v0.1

Evidence status is deliberately conservative. `CONFIRMED` means corroborated by established technical/reference material; emulator behavior remains `PENDING` until reproduced in the selected runtime.

## RNG architecture

- **CONFIRMED (BW technical model):** Generation V uses a 64-bit initial seed. Established BW RNG documentation describes the upper half seeding a Mersenne Twister used for IV generation; PID-related generation is handled separately, breaking the Gen III/IV assumption that PID and IVs are coupled by one universal generation method.
- **CONFIRMED:** Practical Gen V tooling distinguishes PIDRNG from the IV RNG stream. PID-side outputs include shiny status/ability/gender and generation-specific nature handling; IV generation must be modeled separately.
- **CONFIRMED:** Wandering NPCs and other actions can advance PIDRNG irregularly; route automation must classify noisy maps and avoid assuming a fixed frame budget.
- **PENDING/EMULATOR:** Exact initial-seed reproducibility, Timer0 behavior, RTC injection, boot timing and savestate semantics in the selected DS emulator.

## Shiny rules

- **CONFIRMED:** Base shiny criterion in Generations III–V uses the XOR-derived shiny value threshold `< 8`, corresponding to base odds 1/8192 absent modifiers/locks.
- **CONFIRMED:** Shiny Charm is introduced in Black 2/White 2, not Black/White. In Gen V it adds two additional personality-value attempts for applicable wild/static and breeding generation, giving approximately 3/8192 for ordinary applicable encounters.
- **CONFIRMED:** Shiny Charm does not universally apply to every acquisition class; gifts/trades/events require per-class eligibility rather than a global modifier assumption.
- **CONFIRMED:** Hidden Grotto encounters are shiny-ineligible under normal game behavior. Specific gifts are also prevented from being shiny; the lock catalogue must enumerate targets individually.
- **PENDING:** Complete per-version shiny-lock registry, including exact implementation boundary and modified/unlocked-mode strategy.

## Emulator vs retail

Current practical guides explicitly separate retail and emulator workflows. Retail calibration depends on console parameters/Timer0 and boot timing, while emulator workflows can expose controllable RTC/launch conditions. Therefore:

1. Do not copy retail timing constants into emulator profiles.
2. Treat `Timer0` and hardware parameter calibration as environment-specific.
3. Build an emulator profile from observed seed/output pairs.
4. Validate savestate restore both before and after generation-sensitive triggers.
5. A state is not `TESTED` merely because a community RNG procedure works on cartridge.

## Roamers

- **CONFIRMED (operational):** BW roamer workflows treat release as a generation-sensitive boundary distinct from later physical encounter/capture.
- **REQUIREMENT:** Story Progression Engine must classify roamer release as `IRREVERSIBLE` until a persistent pre-release checkpoint exists and the generation method is validated.
- **PENDING:** Exact emulator-specific advances at release and reproducibility after savestate restore.

## Sources registered

- Smogon University — BW RNG Manipulation Guide, Parts 1/3 (technical/practical RNG model).
- PokemonRNG — current BW/B2W2 retail and emulator guides (operational reproduction evidence; environment-specific claims require experiment).
- Bulbapedia — Shiny Pokémon / Shiny Charm reference pages (mechanics catalogue; technical claims should be cross-checked where implementation details matter).

## Next experiments

When a legitimate Gen V ROM/save and selected DS emulator environment are available:

1. identify ROM revision/hash;
2. freeze RTC/launch conditions and collect repeated initial-seed observations;
3. measure seed stability and any Timer0-equivalent variability;
4. isolate PIDRNG vs IV RNG advances with known actions;
5. test `ENCOUNTER_RAW` restoration before/after generation boundary for wild/static/roamer classes;
6. compare observed outputs against PokeFinder/RNG Reporter predictions;
7. promote only reproduced claims to `TESTED`.
