import random
from app.main import get_human_age


def test_should_return_list() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_another_stage_of_animals_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_second_stage_of_animals_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_another1_stage_of_animals_year() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_should_return_third_stage_of_animals_year() -> None:
    assert get_human_age(28, 30) == [3, 3]


def test_with_random_ages_animals() -> None:
    assert get_human_age(random.randint(1, 50), random.randint(1, 50))
