import pytest

from app.main import get_human_age


def test_should_return_zero_human_age() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_first_year_animal_life() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_first_year_animal_life_ceil_value() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_second_year_animal_life() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_second_year_animal_life_ceil_value() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_last_each_year_animal_life_for_cat() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_last_each_year_animal_life_for_dog() -> None:
    assert get_human_age(29, 29) == [3, 3]


def test_last_each_year_animal_life_for_big_numbers() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_receive_string_value() -> None:
    with pytest.raises(TypeError):
        get_human_age("29", "29")
