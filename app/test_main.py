import pytest
from app.main import get_human_age

def test_get_human_age():
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(15, 0) == [1, 0]
    assert get_human_age(24, 0) == [2, 0]
    assert get_human_age(28, 0) == [3, 0]
    assert get_human_age(32, 0) == [4, 0]
    assert get_human_age(36, 0) == [5, 0]
    assert get_human_age(0, 15) == [0, 1]
    assert get_human_age(0, 24) == [0, 2]
    assert get_human_age(0, 29) == [0, 3]
    assert get_human_age(0, 34) == [0, 4]
    assert get_human_age(0, 39) == [0, 5]
    assert get_human_age(28, 29) == [3, 3]
    assert get_human_age(36, 39) == [5, 5]
