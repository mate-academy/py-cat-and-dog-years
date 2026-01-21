import pytest
from app.main import get_human_age


def test_should_calculate_14_cat_or_dog_years_correctly() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_calculate_23_cat_or_dog_years_correctly() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_calculate_28_cat_and_29_dog_years_correctly() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_negative_input() -> None:
    assert get_human_age(-1, -5) == [0, 0]


def test_input_equals_0() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_float_input() -> None:
    assert get_human_age(50.2, 180.0) == [8.0, 33.0]


def test_input_of_wrong_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("cat", {})
