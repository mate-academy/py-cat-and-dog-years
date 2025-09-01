from app.main import get_human_age


def test_under_fifteen() -> None:
    assert (
        get_human_age(0, 0) == [0, 0]
    ), "Ages under 15 should return zeros."


def test_1() -> None:
    assert (
        get_human_age(14, 14) == [0, 0]
    ), "Ages under 15 should return zeros."


def test_2() -> None:
    assert (
        get_human_age(15, 15) == [1, 1]
    ), "Ages under 15 should return zeros."


def test_3() -> None:
    assert (
        get_human_age(23, 23) == [1, 1]
    ), "Ages under 15 should return zeros."


def test_4() -> None:
    assert (
        get_human_age(24, 24) == [2, 2]
    ), "Ages under 15 should return zeros."


def test_5() -> None:
    assert (
        get_human_age(100, 100) == [21, 17]
    ), "Ages under 15 should return zeros."
