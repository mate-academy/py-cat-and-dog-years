import pytest
from app.main import get_human_age

def test_zero_age():
    assert get_human_age(0, 0) == [0, 0]

def test_less_than_first_year():
    assert get_human_age(14, 14) == [0, 0]

def test_exactly_first_year():
    assert get_human_age(15, 15) == [1, 1]

def test_between_first_and_second_year():
    assert get_human_age(23, 23) == [1, 1]

def test_exactly_second_year():
    assert get_human_age(24, 24) == [2, 2]

def test_after_second_year_but_not_enough_for_extra_year():
    assert get_human_age(27, 27) == [2, 2]

def test_exactly_one_extra_year_for_cat():
    assert get_human_age(28, 28) == [3, 2]

def test_large_age():
    assert get_human_age(100, 100) == [21, 17]

def test_only_cat_age():
    assert get_human_age(60, 0) == [11, 0]

def test_only_dog_age():
    assert get_human_age(0, 60) == [0, 9]

def test_boundary_conditions():
    assert get_human_age(16, 16) == [1, 1]
    assert get_human_age(25, 25) == [2, 2]
    assert get_human_age(29, 29) == [3, 3]
