from app.main import get_human_age


def test_should_return_zeros_when_cat_and_dog_age_zeros() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_one_human_year_for_15_cat_and_dog_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_one_human_year_for_23_cat_and_dog_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_human_year_for_24_cat_and_dog_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_two_human_year_for_27_cat_and_28_dog_years() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_should_return_three_human_year_for_28_cat_and_29_dog_years() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_should_return_21_human_years_for_100_cat_and_17_dog_years() -> None:
    assert get_human_age(100, 100) == [21, 17]
