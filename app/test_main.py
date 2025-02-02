import pytest
from app.main import get_human_age

def test_zero_age():
    assert get_human_age(0, 0) == [0, 0]

def test_below_15():
    assert get_human_age(14, 14) == [0, 0]

def test_exactly_15():
    assert get_human_age(15, 15) == [1, 1]

def test_exactly_24():
    assert get_human_age(24, 24) == [2, 2]

def test_first_increase():
    assert get_human_age(28, 28) == [3, 2]

def test_large_values():
    assert get_human_age(100, 100) == [21, 17]
