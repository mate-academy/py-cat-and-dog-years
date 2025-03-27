import pytest
from app.main import get_human_age

def test_get_human_age():
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(16, 16) == [2, 2]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(25, 25) == [3, 3]
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(9, 9) == [0, 0]
    assert get_human_age(30, 35) == [4, 5]
    assert get_human_age(100, 100) == [21, 22]
    assert get_human_age(10, 50) == [0, 7]
    assert get_human_age(100, 10) == [21, 0]
