from app.main import get_human_age


def test_should_return_zeros_if_years_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_1_humans_years_if_animals_years_equal_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_convert_cats_and_dogs_years_into_1_human_age() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_2_if_years_equal_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_convert_cats_and_dogs_years_into_3_human_age() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_should_return_number_of_years_corresponding_animal() -> None:
    assert get_human_age(50, 50) == [8, 7]
