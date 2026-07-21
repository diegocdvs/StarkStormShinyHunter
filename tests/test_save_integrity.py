from starkstorm_shinyhunter.save_integrity import section_checksum, validate_save, SAVE_SIZE


def test_checksum_zero_section():
    assert section_checksum(bytes(3968), 3968) == 0


def test_reject_wrong_save_size():
    try:
        validate_save(bytes(SAVE_SIZE - 1))
    except ValueError:
        pass
    else:
        raise AssertionError("wrong save size must be rejected")


def test_blank_save_is_not_valid():
    report = validate_save(bytes(SAVE_SIZE))
    assert not report["A"]["valid"]
    assert not report["B"]["valid"]
