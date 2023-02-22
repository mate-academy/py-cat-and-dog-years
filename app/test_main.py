from app.main import get_human_age


def test_both_ages_equals_to_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_age_less_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_age_less_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_age_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_age_more_then_29() -> None:
    assert get_human_age(100, 100) == [21, 17]
