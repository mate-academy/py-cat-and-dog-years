import pytest
from app.main import get_human_age


def test_should_return_zeros_when_pets_years_are_zeros() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zeros_when_pets_years_are_less_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_when_pets_years_are_less_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_different_human_years_when_pets_years_are_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_zero_when_data_is_negative_number() -> None:
    assert get_human_age(- 5, 25) == [0, 2]


def test_should_return_expected_result_when_data_is_large_number() \
        -> None:
    assert get_human_age(250, 30) == [58, 3]


def test_should_raise_error_if_data_is_str() -> None:
    cat_age = "5"
    with pytest.raises(TypeError):
        get_human_age(cat_age, 5)
