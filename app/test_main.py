from app.main import get_human_age


def test_returns_zeros_when_age_is_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_returns_zeros_when_age_is_under_15_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_returns_ones_when_age_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_returns_two_when_age_is_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat_age_increases_every_4_years_after_24() -> None:
    assert get_human_age(28, 0) == [3, 0]


def test_dog_age_increases_every_5_years_after_24() -> None:
    assert get_human_age(0, 29) == [0, 3]


def test_returns_correct_human_age_for_cat_and_dog() -> None:
    assert get_human_age(100, 100) == [21, 17]
