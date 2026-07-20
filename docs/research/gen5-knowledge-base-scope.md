# Generation V Knowledge Base — Scope v0.1

Games:
- Pokémon Black
- Pokémon White
- Pokémon Black 2
- Pokémon White 2

## Matrix dimensions

For each game/version/region, record:

1. ROM identity/checksum and revision.
2. Save format and integrity rules.
3. TID/SID/PID/shiny relationships.
4. Initial seed inputs and timing model.
5. Timer0 and other hardware-dependent variability.
6. RNG streams and their roles (IVs, PID, encounter generation, NPC advances, etc.).
7. Encounter categories: wild, static, gift, egg, roamer, phenomena/special encounters.
8. Shiny locks and unlock strategy classification.
9. Shiny Charm applicability in B2W2.
10. RTC/date/time dependence.
11. Emulator-specific behavior and determinism.
12. Savestate semantics and encounter reproducibility.
13. Capture-risk database and required team preparation.
14. Ball policy and availability.
15. Known tools/implementations and reproducibility evidence.

## Emulator validation gate

Retail-cartridge RNG instructions must not be treated as emulator specifications. Hardware-sensitive mechanics remain `PENDING` until tested on the selected DS emulator with controlled RTC, boot timing and savestate experiments.

## Deliverables

- BW technical profile.
- B2W2 technical profile.
- DS emulator comparison/benchmark.
- Gen V RNG test-vector set.
- Encounter-generation method map.
- Shiny-lock catalogue.
- Capture-readiness matrix.
- Savestate determinism report.
