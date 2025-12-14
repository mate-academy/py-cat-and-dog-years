import pytest

from app.main import get_human_age


def test_should_return_zero_for_zero_age():
    assert get_human_age(0, 0) == [0, 0]


def test_cat_dog_younger_than_first_threshold():
    assert get_human_age(14, 14) == [0, 0]


def test_cat_dog_first_human_year():
    assert get_human_age(15, 15) == [1, 1]


def test_between_first_and_second_threshold():
    assert get_human_age(23, 23) == [1, 1]


def test_cat_dog_second_human_year():
    assert get_human_age(24, 24) == [2, 2]


def test_cat_dog_between_second_and_third_threshold():
    assert get_human_age(27, 27) == [2, 2]


def test_cat_dog_after_third_threshold():
    assert get_human_age(28, 28) == [3, 2]


def test_cat_dog_with_big_ages():
    assert get_human_age(100, 100) == [21, 17]


def test_cat_human_age_independent_of_dog() -> None:
    assert get_human_age(32, 34)[0] == 4
    assert get_human_age(32, 10)[0] == 4


def test_dog_human_age_independent_of_cat() -> None:
    assert get_human_age(40, 39)[1] == 5
    assert get_human_age(5, 39)[1] == 5
