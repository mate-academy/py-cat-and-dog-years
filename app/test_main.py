from app.main import get_human_age


def test_should_return_zero_if_age_less_then_one_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_if_age_less_then_two_years() -> None:
    assert get_human_age(16, 16) == [1, 1]


def test_should_return_different_years_if_ages_are_one_hundred() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_should_return_same_years_if_ages_are_different() -> None:
    assert get_human_age(27, 28) == [2, 2]
