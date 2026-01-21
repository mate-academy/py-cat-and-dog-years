import pytest
from app.main import get_human_age


def test_function_returns_a_list_of_two_elements() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_zeros_when_cat_dog_year_is_less_1_human_year() -> None:
    assert get_human_age(1, 14) == [0, 0]


def test_should_return_one_when_anml_year_less_than_sum_1_2_h_year() -> None:
    assert get_human_age(23, 16) == [1, 1]


def test_should_return_zeros_when_cat_dog_year_is_less_or_equal_0() -> None:
    assert get_human_age(0, -5) == [0, 0]


def test_should_raise_error_if_function_get_non_integer() -> None:
    with pytest.raises(TypeError):
        get_human_age({}, "5 years")
