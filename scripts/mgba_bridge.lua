-- StarkStormShinyHunter mGBA bridge v0.1
-- This script deliberately exposes only a narrow, auditable command surface.
-- It is not yet a network daemon; PoC 1 will validate behavior interactively first.

local function require_emulator()
    if emu == nil then
        error("No game is loaded in mGBA")
    end
end

function ssh_game_info()
    require_emulator()
    return {
        title = emu:getGameTitle(),
        platform = emu:platform(),
        rom_size = emu:romSize(),
    }
end

function ssh_read_u8(address)
    require_emulator()
    return emu:read8(address)
end

function ssh_read_u16(address)
    require_emulator()
    return emu:read16(address)
end

function ssh_read_u32(address)
    require_emulator()
    return emu:read32(address)
end

function ssh_run_frame()
    require_emulator()
    emu:runFrame()
end

function ssh_set_keys(mask)
    require_emulator()
    emu:setKeys(mask)
end

function ssh_reset()
    require_emulator()
    emu:reset()
end

function ssh_save_state(path)
    require_emulator()
    -- ALL includes screenshot, save data, cheats, RTC, and metadata.
    -- The exact flags used by production checkpoints will be frozen only after
    -- encounter-boundary determinism is experimentally validated.
    return emu:saveStateFile(path, C.SAVESTATE.ALL)
end

function ssh_load_state(path)
    require_emulator()
    return emu:loadStateFile(path, C.SAVESTATE.ALL)
end

function ssh_screenshot(path)
    require_emulator()
    emu:screenshot(path)
end

console:log("StarkStormShinyHunter mGBA bridge loaded")
