from app.main import get_human_age


def test_cat_and_dog_age_equal_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_cat_and_dog_age_less_than_one_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_cat_and_dogs_age_equal_one_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_cat_and_dogs_age_less_than_two_human_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_cat_and_dogs_age_equal_two_human_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat_and_dogs_age_equal_three_human_years() -> None:
    assert get_human_age(28, 29) == [3, 3]
