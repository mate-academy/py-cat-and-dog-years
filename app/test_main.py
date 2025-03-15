from app.main import get_human_age


def test_should_return_zero_if_age_under_fifteen() -> None:
    assert get_human_age(13, 13) == [0, 0]


def test_should_return_one_for_first_fifteen_years() -> None:
    assert get_human_age(23, 20) == [1, 1]


def test_should_return_two_for_next_nine_years() -> None:
    assert get_human_age(26, 24) == [2, 2]


def test_should_return_one_extra_year_for_every_four_years_cats_life() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_one_extra_year_for_every_five_years_dogs_life() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_large_numbers() -> None:
    assert get_human_age(100, 100) == [21, 17]
