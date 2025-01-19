from app.main import get_human_age


def test_get_human_age_for_returning_zeros() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_one_human_age() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_two_human_age() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_two_human_age_if_the_third_years_are_not_complete() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_get_three_human_age() -> None:
    assert get_human_age(28, 29) == [3, 3]
