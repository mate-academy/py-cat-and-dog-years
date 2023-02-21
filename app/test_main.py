import pytest

from app.main import get_human_age


def test_both_years_under_15_give_0_human_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_both_first_15_years_give_1_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_9_next_years_for_both_give_1_more_human_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_every_4_next_cat_years_give_1_human_year() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_every_5_next_dog_years_give_1_human_year() -> None:
    assert get_human_age(27, 29) == [2, 3]


def test_should_return_0_if_years_are_negative_or_zero() -> None:
    assert get_human_age(-5, 0) == [0, 0]


def test_should_return_years_if_animal_years_are_very_large() -> None:
    assert get_human_age(100000, 9999999) == [24996, 1999997]


def test_should_raise_error_when_passed_not_integer_to_age() -> None:
    with pytest.raises(TypeError):
        get_human_age("Hello", 3.5)
