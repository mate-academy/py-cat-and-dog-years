from app.main import get_human_age


def test_get_human_age_for_both_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_for_near_first_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_exact_first_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_near_second_human_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_exact_second_human_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_after_second_human_year() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_get_human_age_cat_more_than_two_human_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_large_values() -> None:
    assert get_human_age(100, 100) == [21, 17]
