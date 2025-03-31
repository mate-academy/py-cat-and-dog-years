from app.main import get_human_age


def test_should_return_zero_if_zero_input() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_if_less_than_cat_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_minimum_non_zero_result() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_max_one_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_min_two_years_result() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_max_two_years_result() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_min_3_year_cat() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_big_input() -> None:
    assert get_human_age(100, 100) == [21, 17]
