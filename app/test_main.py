import pytest
from app.main import get_human_age


def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_under_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_first_human_age() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_second_threshould() -> None:
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]


def test_cat_extra_years() -> None:
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]


def test_large_values() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_negative_values() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, 10)
    with pytest.raises(ValueError):
        get_human_age(10, -5)


def test_invalid_types() -> None:
    with pytest.raises(TypeError):
        get_human_age("ten", 10)
    with pytest.raises(TypeError):
        get_human_age(10, "five")
