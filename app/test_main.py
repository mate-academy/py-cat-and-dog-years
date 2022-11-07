from app.main import get_human_age
import pytest


def test_should_return_0_human_age_when_animal_age_less_than_15():
    assert(
        get_human_age(14, 14) == [0, 0]
    )


def test_should_return_1_human_age_when_animal_age_less_than_24():
    assert (
            get_human_age(23, 23) == [1, 1]
    )


def test_should_return_2_human_age_when_animal_age_equal_24():
    assert (
            get_human_age(24, 24) == [2, 2]
    )


def test_should_return_2_human_age_when_cat_dog_age_equal_27_28():
    assert (
            get_human_age(27, 28) == [2, 2]
    )


def test_should_return_3_human_age_when_cat_dog_age_equal_28_29():
    assert (
            get_human_age(28, 29) == [3, 3]
    )


def test_should_return_0_human_age_when_animal_age_negative():
    assert (
            get_human_age(-76, -65) == [0, 0]
    )


def test_should_return_0_human_age_when_animal_age_equal_0():
    assert (
            get_human_age(0, 0) == [0, 0]
    )


def test_should_raise_error_if_function_receives_an_incorrect_type_of_data():
    with pytest.raises(TypeError):
        get_human_age("0", "56")
