from app.main import get_human_age


def test_result_should_be_zeroes_if_given_age_is_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_result_should_be_zeroes_if_given_age_is_less_than_one_animal_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_result_should_be_one_year_when_given_humans_years_are_equal_to_one() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_result_should_be_one_year_when_given_humans_year_between_one_and_two_animal_years() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_result_sohuld_be_one_year_when_given_humans_year_equals_two_animal_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_result_should_be_different_for_different_animals_when_age_is_not_equal() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_result_should_return_correct_animals_years_when_arguments_are_different() -> None:
    assert get_human_age(62, 74) == [11, 12]
