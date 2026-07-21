# Gen V — Emulator Validation Risks v0.1

## Status
Sprint 0 research note. No Gen V emulator-dependent RNG behavior is considered `TESTED` yet.

## Confirmed external constraint
Current retail Black/White RNG guidance documents seed targeting through console date/time, launch timing, keypresses and game-profile calibration, with `Timer0` variability as a failure mode. The same guidance explicitly warns that its procedure is for cartridges and is not directly portable to alternative execution environments.

## Architectural consequence
The project must not copy retail-hardware timing recipes into an emulator worker and assume equivalence. Gen V requires an emulator-specific calibration/validation layer before automation.

## Required experiments per exact game/revision/emulator
1. Identify ROM revision/hash without storing ROM bytes in Git.
2. Identify emulator and version; record RTC configuration.
3. Determine whether boot/reset reproduces initial-seed behavior under controlled RTC/time inputs.
4. Measure seed/Timer0-like variability observable in the emulated environment.
5. Determine which RNG streams/state variables can be observed reliably.
6. Validate save-state restoration around boot, overworld, encounter generation and protected triggers.
7. Re-run identical state/input sequences to test determinism.
8. Compare predicted vs observed PID/IV/nature/ability/gender/shiny attributes for each supported encounter class.

## Gate
No Gen V hunt method may be promoted from `PARTIAL/PENDING` to `TESTED` until the exact emulator execution path reproduces predicted results repeatedly. Hardware-only guides remain research references, not executable specifications.

## Source provenance
- pokemonrng.com retail Black/White Starter RNG guide, updated 2026-03-29: documents launch timing, configured game profile, initial seed targeting, keypresses and Timer0 variability; explicitly scoped to cartridge workflows.
- PokeFinder is treated as a comparison/reference implementation where applicable, not as proof that our emulator timing model is correct.

## Open decisions deferred until evidence exists
- DS emulator selection for production worker.
- Whether boot-time seed manipulation or direct observable RNG-state targeting is the more robust automation strategy.
- Cloud determinism and RTC virtualization strategy.
