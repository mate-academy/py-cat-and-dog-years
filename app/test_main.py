from app.main import get_human_age


def test_with_age_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_with_age_less_than_first_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_with_age_equal_to_first_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_with_age_less_than_two() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_with_age_equal_to_two() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_with_age_less_than_three() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_with_cat_age_equal_to_three() -> None:
    assert get_human_age(27, 27) == [3, 2]


def test_with_both_ages_equal_to_100() -> None:
    assert get_human_age(100, 100) == [21, 17]
