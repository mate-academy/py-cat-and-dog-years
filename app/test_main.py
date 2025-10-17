import pytest
from app.main import get_human_age


def test_zero_ages() -> None:
    """Test that both zero ages return [0, 0]."""
    assert get_human_age(0, 0) == [0, 0]


def test_less_than_first_threshold() -> None:
    """Test ages below the first threshold (15)."""
    assert get_human_age(14, 14) == [0, 0]


def test_exactly_first_threshold() -> None:
    """Test ages exactly equal to 15 give one human year."""
    assert get_human_age(15, 15) == [1, 1]


def test_between_first_and_second_threshold() -> None:
    """Test that age between 15 and 24 gives one human year."""
    assert get_human_age(23, 23) == [1, 1]


def test_exactly_second_threshold() -> None:
    """Test that age 24 gives two human years."""
    assert get_human_age(24, 24) == [2, 2]


def test_between_second_and_third_threshold() -> None:
    """Test that ages between 24 and 28 for cat, 29 for dog behave."""
    assert get_human_age(27, 27) == [2, 2]


def test_extra_human_years_after_thresholds() -> None:
    """Test that ages above second threshold add correctly."""
    assert get_human_age(28, 28) == [3, 2]


def test_large_values() -> None:
    """Test large values of cat and dog age conversion."""
    assert get_human_age(100, 100) == [21, 17]


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (44, 44, [7, 6]),
    ],
)
def test_parametrized_cases(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    """Test multiple conversion scenarios with parameterization."""
    assert get_human_age(cat_age, dog_age) == expected
