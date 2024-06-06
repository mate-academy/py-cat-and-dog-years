from app.main import get_human_age
import pytest


def test_when_years_is_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(9, 0) == [0, 0]
    assert get_human_age(0, 9) == [0, 0]


def test_when_age_is_too_low_for_cat() -> None:
    assert get_human_age(14, 16) == [0, 1]
    assert get_human_age(9, 24) == [0, 2]
    assert get_human_age(4, 29) == [0, 3]


def test_when_age_is_too_low_for_dog() -> None:
    assert get_human_age(16, 14) == [1, 0]
    assert get_human_age(24, 9) == [2, 0]
    assert get_human_age(28, 4) == [3, 0]


def test_when_age_close_to_two() -> None:
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(23, 14) == [1, 0]
    assert get_human_age(14, 23) == [0, 1]


def test_for_big_numbers() -> None:
    assert get_human_age(100, 100) == [21, 17]
    assert get_human_age(150, 150) == [33, 27]


if __name__ == "__main__":
    pytest.main()
