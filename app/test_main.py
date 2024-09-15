from app.main import get_human_age


def test_the_age_of_the_cat_and_dog_is_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_age_of_cat_and_dog_up_to_fifteen_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_the_first_fifteen_years_of_animals() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_the_next_nine_years_of_animals() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_the_next_full_nine_years_of_animals() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_the_next_four_years_of_animals() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_the_next_full_years_of_a_cat_and_half_a_year_of_a_dog() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_if_you_give_100_years_to_animals() -> None:
    assert get_human_age(100, 100) == [21, 17]
