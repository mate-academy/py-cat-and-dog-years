import pytest
from app.main import get_human_age


def test_should_return_0_if_animal_age_is_0():
    result = get_human_age(0, 0)
    assert result == [0, 0]


def test_should_return_0_if_animal_age_is_less_than_15():
    result = get_human_age(14, 14)
    assert result == [0, 0]


def test_should_return_1_if_animal_age_is_15():
    result = get_human_age(15, 15)
    assert result == [1, 1]


def test_should_return_1_if_animal_age_is_more_than_14_and_less_than_24():
    result = get_human_age(23, 23)
    assert result == [1, 1]


def test_should_return_2_if_animal_age_is_24():
    result = get_human_age(24, 24)
    assert result == [2, 2]


def test_should_return_correct_age_if_animal_age_is_more_than_24():
    result = get_human_age(100, 100)
    assert result == [21, 17]


def test_should_raise_error_if_any_of_animal_age_not_an_integer():
    with pytest.raises(TypeError):
        get_human_age("haha", 100)
