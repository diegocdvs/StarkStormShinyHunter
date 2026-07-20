from starkstorm_shinyhunter.rng.gen3_lcrng import Gen3LCRNG, is_shiny


def test_seed_zero_known_sequence() -> None:
    rng = Gen3LCRNG(0)
    expected = [
        0x00006073,
        0xE97E7B6A,
        0x52713895,
        0x31B0DDE4,
        0x8E425287,
    ]
    observed = [rng.advance() for _ in expected]
    assert observed == expected


def test_next_u16_returns_high_half_after_advance() -> None:
    rng = Gen3LCRNG(0)
    assert rng.next_u16() == 0x0000
    assert rng.next_u16() == 0xE97E


def test_clone_is_independent() -> None:
    rng = Gen3LCRNG(0)
    rng.advance(3)
    clone = rng.clone()
    assert clone.state == rng.state
    clone.advance()
    assert clone.state != rng.state


def test_shiny_predicate_boundary() -> None:
    tid = 0
    sid = 0
    assert is_shiny(tid=tid, sid=sid, pid=0x00000000)
    assert is_shiny(tid=tid, sid=sid, pid=0x00000007)
    assert not is_shiny(tid=tid, sid=sid, pid=0x00000008)


def test_negative_advance_rejected() -> None:
    rng = Gen3LCRNG(0)
    try:
        rng.advance(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("negative advance must raise ValueError")
