from app.main import get_human_age


def test_get_human_age_when_0_0() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_when_14_14() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_when_23_23() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_when_24_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_when_100_100() -> None:
    assert get_human_age(100, 100) == [21, 17]
