import pytest
from app.main import get_human_age


def test_should_return_expected_animal_ages() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_when_cat_age_is_less_than_0() -> None:
    assert get_human_age(-10, 23) == [0, 1]


def test_when_dog_age_is_less_than_0() -> None:
    assert get_human_age(23, -1) == [1, 0]


def test_should_return_0_when_both_ages_is__0() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_when_function_resive_realy_large_numbers() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_should_raise_error_if_incorrect_data_type() -> None:
    with pytest.raises(TypeError):
        assert get_human_age("sf", [])
