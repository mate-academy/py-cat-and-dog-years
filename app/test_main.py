import pytest
from app.main import get_human_age


def test_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0],\
        f"Expected [0, 0], but got {get_human_age(0, 0)}"
    assert get_human_age(0, 10) == [0, 0],\
        f"Expected [0, 0], but got {get_human_age(0, 10)}"
    assert get_human_age(10, 0) == [0, 0],\
        f"Expected [0, 0], but got {get_human_age(10, 0)}"


def test_first_year_age() -> None:
    assert get_human_age(1, 1) == [0, 0],\
        f"Expected [0, 0], but got {get_human_age(1, 1)}"
    assert get_human_age(14, 14) == [0, 0],\
        f"Expected [0, 0], but got {get_human_age(14, 14)}"
    assert get_human_age(15, 15) == [1, 1],\
        f"Expected [1, 1], but got {get_human_age(15, 15)}"


def test_second_year_age() -> None:
    assert get_human_age(16, 16) == [1, 1],\
        f"Expected [1, 1], but got {get_human_age(16, 16)}"
    assert get_human_age(23, 23) == [1, 1],\
        f"Expected [1, 1], but got {get_human_age(23, 23)}"
    assert get_human_age(24, 24) == [2, 2],\
        f"Expected [2, 2], but got {get_human_age(24, 24)}"


def test_additional_years() -> None:
    assert get_human_age(28, 28) == [3, 2],\
        f"Expected [3, 2], but got {get_human_age(28, 28)}"
    assert get_human_age(32, 32) == [4, 3],\
        f"Expected [4, 3], but got {get_human_age(32, 32)}"
    assert get_human_age(100, 100) == [21, 17],\
        f"Expected [21, 17], but got {get_human_age(100, 100)}"


def test_large_ages() -> None:
    assert get_human_age(50, 50) == [8, 7],\
        f"Expected [8, 7], but got {get_human_age(50, 50)}"
    assert get_human_age(75, 75) == [14, 12],\
        f"Expected [14, 12], but got {get_human_age(75, 75)}"


def test_edge_cases() -> None:
    assert get_human_age(15, 0) == [1, 0],\
        f"Expected [1, 0], but got {get_human_age(15, 0)}"
    assert get_human_age(0, 15) == [0, 1],\
        f"Expected [0, 1], but got {get_human_age(0, 15)}"
    assert get_human_age(16, 14) == [1, 0],\
        f"Expected [1, 0], but got {get_human_age(16, 14)}"


if __name__ == "__main__":
    pytest.main()
