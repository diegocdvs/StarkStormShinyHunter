# Emulator Adapter Contract — v0.1

This contract defines the minimum capabilities required from any emulator integration.

## Required operations

```text
load_game(source)
load_save(source, temporary=false)
read_memory(address, length)
write_memory(address, data)
press(button)
hold(button, frames)
release(button)
run_frame(count=1)
step_instruction(count=1)
reset()
save_state(destination, flags=ALL)
load_state(source, flags=SAFE_RESTORE)
screenshot(destination)
rom_checksum()
game_code()
game_title()
current_frame()
```

## Required events

- emulator started;
- frame completed;
- input read;
- reset;
- save data updated;
- crash;
- shutdown/stop.

## Safety invariants

1. `ENCOUNTER_RAW` is immutable after creation.
2. A state may not be considered a valid encounter checkpoint until a restore test demonstrates that it reproduces the same encounter identity and relevant RNG state.
3. Save-state persistence and normal in-game save persistence are separate mechanisms.
4. No adapter may overwrite the sole valid `.sav`.
5. ROM revision/checksum must be recorded before any address map, patch, or game-specific adapter is activated.
6. Every write-capable operation must be auditable in logs.

## mGBA mapping

The official mGBA Lua API provides direct equivalents for the required GBA PoC primitives, including memory access, button state, frame/instruction stepping, reset, savestates, screenshots, callbacks, checksum and ROM metadata.

## Cloud caveat

Do not assume background/headless operation. Deployment mode is a benchmark item. A virtual display or alternative execution architecture may be required depending on the tested mGBA build.
