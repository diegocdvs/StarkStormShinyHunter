from __future__ import annotations

from dataclasses import dataclass

MASK_32 = 0xFFFFFFFF
MULTIPLIER = 0x41C64E6D
INCREMENT = 0x00006073


@dataclass(slots=True)
class Gen3LCRNG:
    """32-bit linear congruential RNG used by Generation III game logic.

    This class intentionally models only the core recurrence. Encounter-specific
    generation methods belong in separate strategy modules because the number and
    order of RNG calls differ by context.
    """

    state: int

    def __post_init__(self) -> None:
        self.state &= MASK_32

    def advance(self, count: int = 1) -> int:
        if count < 0:
            raise ValueError("count must be non-negative")
        for _ in range(count):
            self.state = (self.state * MULTIPLIER + INCREMENT) & MASK_32
        return self.state

    def next_u16(self) -> int:
        return self.advance() >> 16

    def clone(self) -> "Gen3LCRNG":
        return Gen3LCRNG(self.state)


def is_shiny(*, tid: int, sid: int, pid: int) -> bool:
    """Return Gen III shiny status from trainer IDs and PID.

    Gen III uses an XOR-derived shiny value; values below 8 are shiny.
    Inputs are masked to their in-game widths so callers cannot accidentally
    leak wider integer state into the calculation.
    """

    tid &= 0xFFFF
    sid &= 0xFFFF
    pid &= MASK_32
    pid_hi = (pid >> 16) & 0xFFFF
    pid_lo = pid & 0xFFFF
    return (tid ^ sid ^ pid_hi ^ pid_lo) < 8
