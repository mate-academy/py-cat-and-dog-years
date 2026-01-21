import pytest
from app.main import get_human_age


def test_should_raise_error_when_input_not_int() -> None:
    with pytest.raises(TypeError):
        get_human_age("16", 15)


def test_should_return_zeros_when_input_is_negative() -> None:
    assert get_human_age(-5, -12) == [0, 0]


def test_should_return_zeros_when_age_is_less_than_15() -> None:
    assert get_human_age(1, 14) == [0, 0]


def test_should_return_ones_when_age_is_more_than_15() -> None:
    assert get_human_age(16, 19) == [1, 1]


def test_should_return_extra_human_year_to_cat_after_age_of_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_extra_human_year_to_dog_after_age_of_29() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_should_return_value_when_ages_are_too_big() -> None:
    assert get_human_age(150, 150) == [33, 27]
