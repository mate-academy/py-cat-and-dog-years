import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        # Both ages = 0
        (0, 0, [0, 0]),

        # Before first threshold
        (1, 1, [0, 0]),
        (14, 14, [0, 0]),

        # Exactly first threshold (15 years -> 1 human year)
        (15, 15, [1, 1]),

        # Between first and second thresholds
        (20, 20, [1, 1]),
        (23, 23, [1, 1]),

        # Exactly second threshold (15 + 9 = 24 years -> 2 human years)
        (24, 24, [2, 2]),

        # After second threshold: incremental conversion
        # Cat: +1 human year every 4 cat years
        # Dog: +1 human year every 5 dog years
        (28, 29, [3, 3]),  # cat: (28-24)//4 = 1 -> 3, dog: (29-24)//5 = 1 -> 3
        (31, 34, [3, 4]),  # cat: (31-24)//4 = 1 -> 3, dog: (34-24)//5 = 2 -> 4

        # Larger values
        (40, 40, [6, 5]),
        (100, 100, [21, 17]),

        # Mixed ages
        (24, 15, [2, 1]),
        (15, 24, [1, 2]),
        (50, 10, [8, 0]),
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -5),
        (-1, -1),
    ],
)
def test_negative_ages(cat_age, dog_age):
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 10),
        (10, "15"),
        ("cat", "dog"),
        (None, 10),
        (10, None),
        ([], {}),
    ],
)
def test_invalid_types(cat_age, dog_age):
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
