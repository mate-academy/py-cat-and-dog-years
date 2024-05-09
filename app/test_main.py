from app.main import get_human_age


def test_should_return_list_with_2_integers() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_convert_animals_14_years_to_one_human() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_convert_animals_23_years_to_1_human() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_convert_animals_24_years_to_2_human() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_convert_cats_27_and_dogs_28_years_to_3_human() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_should_convert_cats_28_and_dogs_29_years_to_3_human() -> None:
    assert get_human_age(28, 29) == [3, 3]
