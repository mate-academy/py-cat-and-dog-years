from app.main import get_human_age


def test_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_age_equals_14() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_age_equals_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_age_equals_23() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_age_equals_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_age_equals_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_age_equals_100() -> None:
    assert get_human_age(100, 100) == [21, 17]
