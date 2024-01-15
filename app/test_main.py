import pytest

from app.main import get_human_age


def test_should_return_zero_when_negative_arguments() -> None:
    assert get_human_age(-1, -2) == [0, 0]


def test_arguments_should_be_int() -> None:
    with pytest.raises(TypeError):
        get_human_age("10", {10})


def test_should_return_zero_if_age_is_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_if_age_is_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_one_if_age_is_23() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_2_if_age_is_27_and_28() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_every_4_years_for_cats_and_every_5_for_dogs() -> None:
    assert get_human_age(28, 29) == [3, 3]
