from app.main import get_human_age


def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_age_lower_than_first_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_ages_are_both_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_ages_are_both_23() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_ages_are_both_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_ages_are_both_26() -> None:
    assert get_human_age(26, 26) == [2, 2]


def test_ages_are_both_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_ages_are_both_100() -> None:
    assert get_human_age(100, 100) == [21, 17]
