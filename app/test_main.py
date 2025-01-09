from app.main import get_human_age


def test_get_human_age_when_both_ages_are_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_when_ages_are_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_when_ages_are_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_when_ages_are_23() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_when_ages_are_24_and_above() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_when_ages_are_100() -> None:
    assert get_human_age(100, 100) == [21, 17]
