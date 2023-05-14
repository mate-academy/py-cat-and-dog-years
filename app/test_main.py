from app.main import get_human_age


def test_when_cat_and_dog_age_is_equal_0() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_when_the_cat_and_dog_age_is_not_enough_to_be_a_year_old() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_when_the_cat_and_dog_are_one_year_old() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_when_the_cat_and_dog_are_not_old_enough_to_be_two_years_old() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_when_the_cat_and_dog_are_two_years_old() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_when_the_cat_and_dog_are_not_old_enough_to_be_3_years_old() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_when_the_cat_is_3_years_old_and_the_dog_is_2_years_old() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_when_a_cat_and_a_dog_are_100_years_old() -> None:
    assert get_human_age(100, 100) == [21, 17]
