from app.main import get_human_age


def test_returns_zero_for_ages_below_first_year() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_returns_one_for_ages_in_second_year_range() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_returns_two_for_ages_in_third_year_range() -> None:
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_returns_correct_age_for_years_after_second_year() -> None:
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]
