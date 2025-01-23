from app.main import get_human_age
import pytest


def test_get_human_age_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_less_than_first_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_equals_to_first_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_between_first_and_second_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_get_human_age_equals_to_second_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_between_second_and_third_year() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_get_human_age_cat_third_year_dog_second_year() -> None:
    assert get_human_age(28, 28) == [3, 2]

def test_get_human_age_larger_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_get_human_age_different_ages() -> None:
    assert get_human_age(30, 40) == [3, 5]
    assert get_human_age(50, 60) == [8, 9]
    assert get_human_age(10, 20) == [0, 1]
