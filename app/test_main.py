import pytest
from typing import Any
from app.main import get_human_age


def test_get_human_age_cat_progression() -> None:
    """Test cat age progression after second threshold (every 4 years)."""
    assert get_human_age(28, 0) == [3, 0]
    assert get_human_age(32, 0) == [4, 0]
    assert get_human_age(36, 0) == [5, 0]


def test_get_human_age_dog_progression() -> None:
    """Test dog age progression after second threshold (every 5 years)."""
    assert get_human_age(0, 29) == [0, 3]
    assert get_human_age(0, 34) == [0, 4]
    assert get_human_age(0, 39) == [0, 5]


def test_get_human_age_remainder_discarded() -> None:
    """Test that remainder is properly discarded (no rounding up)."""
    assert get_human_age(26, 26) == [2, 2]
    assert get_human_age(30, 26) == [3, 2]


def test_get_human_age_result_format() -> None:
    """Test that result is a list with exactly 2 integer elements."""
    result = get_human_age(25, 30)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(age, int) for age in result)


def test_get_human_age_negative_inputs() -> None:
    """Test behavior with negative age inputs."""
    assert get_human_age(-1, 5) == [0, 0]
    assert get_human_age(5, -1) == [0, 0]
    assert get_human_age(-5, -10) == [0, 0]
    assert get_human_age(-1, 25) == [0, 2]


@pytest.mark.parametrize("cat_age, dog_age, expected_or_error", [
    (3.5, 5, [0, 0]),  # Float values work, truncated in comparisons
    (5, 3.5, [0, 0]),
    (25.8, 30.2, [2, 3]),  # Float values converted properly
])
def test_get_human_age_float_inputs(
    cat_age: Any, dog_age: Any, expected_or_error: list[int]
) -> None:
    """Test behavior with float input values."""
    assert get_human_age(cat_age, dog_age) == expected_or_error


@pytest.mark.parametrize("cat_age, dog_age, error_type", [
    ("5", 10, TypeError),
    (10, "5", TypeError),
    (None, 5, TypeError),
    (5, None, TypeError),
])
def test_get_human_age_incorrect_types(
    cat_age: Any, dog_age: Any, error_type: type
) -> None:
    """Test that incorrect input types raise appropriate exceptions."""
    with pytest.raises(error_type):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (1, 1, [0, 0]),
    (14, 14, [0, 0]),
    (10, 5, [0, 0]),
    (15, 15, [1, 1]),
    (16, 16, [1, 1]),
    (20, 20, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (25, 25, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (29, 29, [3, 3]),
    (50, 30, [8, 3]),
    (30, 50, [3, 7]),
    (100, 100, [21, 17]),
])
def test_get_human_age_examples(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:

    assert get_human_age(cat_age, dog_age) == expected
