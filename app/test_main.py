from app.main import get_human_age
import pytest


def test_get_human_age() -> None:
    assert get_human_age(0, 0) == [1, 1]
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(30, 30) == [3, 3]
    assert get_human_age(50, 50) == [5, 5]
    assert get_human_age(100, 100) == [10, 10]


def test_get_human_age_edge_cases() -> None:
    assert get_human_age(0, 0) == [1, 1]
    assert get_human_age(1, 1) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(16, 16) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(25, 25) == [2, 2]
    assert get_human_age(34, 34) == [3, 3]
    assert get_human_age(35, 35) == [3, 3]
    assert get_human_age(44, 44) == [4, 4]
    assert get_human_age(45, 45) == [4, 4]
    assert get_human_age(54, 54) == [5, 5]


def test_get_human_age_invalid_inputs() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, 10)
    with pytest.raises(ValueError):
        get_human_age(10, -1)
    with pytest.raises(ValueError):
        get_human_age(-5, -5)
