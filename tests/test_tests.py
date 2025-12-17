import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
        (1000, 1000, [246, 197]),
    ],
)
def test_get_human_age_valid_values(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    """Checks correct age conversion for valid input values."""
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_prev, cat_next",
    [
        (14, 15),
        (23, 24),
        (27, 28),
    ],
)
def test_cat_output_changes_on_boundaries(
    cat_prev: int,
    cat_next: int,
) -> None:
    """Ensures cat human age increases exactly at boundary points."""
    prev_value = get_human_age(cat_prev, 0)[0]
    next_value = get_human_age(cat_next, 0)[0]
    assert prev_value != next_value


@pytest.mark.parametrize(
    "dog_prev, dog_next",
    [
        (14, 15),
        (23, 24),
        (28, 29),
    ],
)
def test_dog_output_changes_on_boundaries(
    dog_prev: int,
    dog_next: int,
) -> None:
    """Ensures dog human age increases exactly at boundary points."""
    prev_value = get_human_age(0, dog_prev)[1]
    next_value = get_human_age(0, dog_next)[1]
    assert prev_value != next_value
