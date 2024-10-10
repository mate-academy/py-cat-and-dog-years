import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (16, 16, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (30, 20, [3, 1])
    ],
    ids=[
        "both zero age",
        "both below first year",
        "both exactly first year",
        "slightly above first year",
        "both exactly second year",
        "both slightly above second year",
        "cat older than dog",
        "both much older",
        "cat and dog different ages"
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    """
    This function tests the get_human_age function with valid inputs.

    :param cat_age: The age of the cat in cat years.
    :param dog_age: The age of the dog in dog years.
    :param expected: The expected output list of ages in human years.
    """
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (1000, 1000, [246, 197]),
        (5000, 5000, [1246, 997])
    ],
    ids=[
        "large values",
        "even larger values"
    ]
)
def test_get_human_age_with_large_values(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    """
    Test get_human_age function with large input values.

    :param cat_age: The age of the cat in cat years (large value).
    :param dog_age: The age of the dog in dog years (large value).
    :param expected: The expected output list of ages in human years.
    """
    assert get_human_age(cat_age, dog_age) == expected
