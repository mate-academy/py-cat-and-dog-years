import pytest
from app.main import get_human_age


def test_should_return_correct_result_if_value_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_correct_result_if_values_less_than_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_correct_result_if_values_equal_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_correct_result_if_values_equal_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_correct_result_if_values_have_extra_years() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_correct_result_if_values_is_big_value() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_should_return_exception_if_values_is_not_list_of_two_integers() -> None:
    with pytest.raises(TypeError):
        get_human_age("5", [2])