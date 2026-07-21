from __future__ import annotations

SECTION_SIZE = 0x1000
SECTION_COUNT = 14
BLOCK_SIZE = SECTION_SIZE * SECTION_COUNT
SAVE_SIZE = 0x20000
SIGNATURE = 0x08012025
CHECKSUM_LENGTHS = {0:3884,1:3968,2:3968,3:3968,4:3848,5:3968,6:3968,7:3968,8:3968,9:3968,10:3968,11:3968,12:3968,13:2000}


def section_checksum(section: bytes, length: int) -> int:
    if length % 4 or len(section) < length:
        raise ValueError("invalid checksum input")
    total = 0
    for i in range(0, length, 4):
        total = (total + int.from_bytes(section[i:i+4], "little")) & 0xFFFFFFFF
    return ((total >> 16) + (total & 0xFFFF)) & 0xFFFF


def validate_block(raw: bytes, offset: int) -> dict:
    reports = []
    for physical in range(SECTION_COUNT):
        s = raw[offset + physical*SECTION_SIZE: offset + (physical+1)*SECTION_SIZE]
        sid = int.from_bytes(s[0xFF4:0xFF6], "little")
        stored = int.from_bytes(s[0xFF6:0xFF8], "little")
        sig = int.from_bytes(s[0xFF8:0xFFC], "little")
        index = int.from_bytes(s[0xFFC:0x1000], "little")
        length = CHECKSUM_LENGTHS.get(sid)
        reports.append({"physical": physical, "section_id": sid, "save_index": index, "signature_ok": sig == SIGNATURE, "checksum_ok": length is not None and section_checksum(s, length) == stored})
    ids = [x["section_id"] for x in reports]
    indices = {x["save_index"] for x in reports}
    valid = sorted(ids) == list(range(SECTION_COUNT)) and len(indices) == 1 and all(x["signature_ok"] and x["checksum_ok"] for x in reports)
    return {"valid": valid, "save_index": next(iter(indices)) if len(indices) == 1 else None, "sections": reports}


def validate_save(raw: bytes) -> dict:
    if len(raw) != SAVE_SIZE:
        raise ValueError(f"expected {SAVE_SIZE} bytes, got {len(raw)}")
    return {"A": validate_block(raw, 0), "B": validate_block(raw, BLOCK_SIZE)}
