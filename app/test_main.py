import pytest  # noqa: F401
from app.main import get_human_age


def test_get_human_age() -> None:
    # Test cases
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]

    # Additional edge cases
    assert get_human_age(16, 16) == [1, 1]  # Just above 15
    assert get_human_age(25, 25) == [2, 2]  # Just above 24
    assert get_human_age(30, 30) == [3, 3]  # Just above 28
    assert get_human_age(50, 50) == [8, 7]  # Midway case
    assert get_human_age(200, 200) == [46, 37]  # Corrected expected output
