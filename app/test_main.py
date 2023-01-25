from app.main import get_human_age


def test_cat_and_dog_years_under_15_should_equal_0_human_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_15_cat_and_dog_years_should_equal_1_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_cat_and_dog_years_under_24_should_equal_1_human_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_24_cat_and_dog_years_should_equal_2_human_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat_and_dog_years_under_28_and_29_should_equal_2_human_year() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_24_cat_and_29_dog_years_should_equal_3_human_years() -> None:
    assert get_human_age(28, 29) == [3, 3]
