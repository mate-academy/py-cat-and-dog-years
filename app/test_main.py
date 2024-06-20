from app.main import get_human_age


def test_get_human_age_zero_years() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_less_than_first_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_exactly_first_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_less_than_second_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_exactly_second_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_more_than_second_year() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_get_human_age_exactly_third_year_for_cat() -> None:
    assert get_human_age(28, 27) == [3, 2]


def test_get_human_age_large_values() -> None:
    assert get_human_age(100, 100) == [21, 17]
