import pytest

from app.main import get_human_age

def test_zero_cat_and_dog_age() -> None:
    assert (get_human_age(0, 0) == [0, 0])

def test_borderline_case_zero_and_one_human_years():
    assert (get_human_age(14, 14) == [0, 0])

def test_for_one_human_age() -> None:
    assert (get_human_age(15, 15) == [1, 1])

def test_for_two_humans_age() -> None:
    assert (get_human_age(24, 24) == [2, 2])

def test_for_the_borderline_case_between_two_and_three_years() -> None:
    assert (get_human_age(27, 27) == [2, 2])

def test_for_three_humans_age() -> None:
    assert (get_human_age(30, 30) == [3, 3])

def test_for_twenty_seven_cat_and_dog_ears() -> None:
    assert (get_human_age(28, 28) == [3, 2])

def test_for_hundred_cat_and_dog_ears() -> None:
    assert (get_human_age(100, 100) == [21, 17])

def test_should_raise_error_if_empty_enter():
    with pytest.raises(TypeError):
        get_human_age()
