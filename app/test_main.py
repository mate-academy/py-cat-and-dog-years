from app.main import get_human_age
import pytest


def test_should_return_0_human_age_when_animal_age_less_than_15() -> None:
    assert (
        get_human_age(14, 14) == [0, 0]
    )


def test_should_return_1_human_age_when_animal_age_less_than_24() -> None:
    assert (
        get_human_age(23, 23) == [1, 1]
    )


def test_should_return_2_human_age_when_animal_age_equal_24() -> None:
    assert (
        get_human_age(24, 24) == [2, 2]
    )


def test_should_return_2_human_age_when_cat_dog_age_equal_27_28() -> None:
    assert (
        get_human_age(27, 28) == [2, 2]
    )


def test_should_return_3_human_age_when_cat_dog_age_equal_28_29() -> None:
    assert (
        get_human_age(28, 29) == [3, 3]
    )


def test_should_return_0_human_age_when_animal_age_negative() -> None:
    assert (
        get_human_age(-76, -65) == [0, 0]
    )


def test_should_return_0_human_age_when_animal_age_equal_0() -> None:
    assert (
        get_human_age(0, 0) == [0, 0]
    )


def test_should_raise_error_if_func_receives_incorrect_type_of_data() -> None:
    with pytest.raises(TypeError):
        get_human_age("0", "56")
