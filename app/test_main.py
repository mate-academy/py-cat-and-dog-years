import pytest

from app.main import get_human_age


def test_cat_and_dog_age_from_0_to_14_should_give_0() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


def test_cat_and_dog_age_from_15_to_23_should_give_1() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_cat_and_dog_age_from_15_to_23_should_give_2() -> None:
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]


def test_age_of_cat_should_become_3_and_dog_should_remain_2() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_correctly_handle_large_numbers() -> None:
    assert get_human_age(1000, 1000) == [246, 197]


def test_should_return_zeroes_when_input_is_negative() -> None:
    assert get_human_age(-1, -10) == [0, 0]


def test_should_raise_type_error_when_input_not_integer() -> None:
    with pytest.raises(TypeError):
        get_human_age("one", 1.1)
