import pytest
from app.main import get_human_age


def test_should_return_cat_years_one_more_for_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_zero_if_years_not_more_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_if_years_not_more_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_zero_for_zero_arguments() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_for_negative_arguments() -> None:
    assert get_human_age(-6, -13) == [0, 0]


def test_should_accept_correct_type_arguments() -> None:
    with pytest.raises(TypeError):
        get_human_age("19", 28)
