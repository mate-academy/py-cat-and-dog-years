from app.main import get_human_age


def test_of_zero_values_of_the_function() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_of_the_max_age_of_an_animal_with_a_zero_value_of_a_human() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_of_the_min_age_of_an_animal_with_a_one_value_of_a_human() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_of_the_max_age_of_an_animal_with_a_one_value_of_a_human() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_of_the_min_age_of_an_animal_with_a_two_value_of_a_human() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_of_the_max_age_of_an_animal_with_a_two_value_of_a_human() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_of_min_values_there_is_a_difference_between_cat_and_dog() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_of_max_age() -> None:
    assert get_human_age(100, 100) == [21, 17]
