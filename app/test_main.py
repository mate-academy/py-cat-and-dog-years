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
        (-5, 10, [0, 0]),
        (5, -10, [0, 0]),
        (-3, -3, [0, 0]),
        (-24, 24, [0, 2])
    ],
    ids=[
        "negative cat age",
        "negative dog age",
        "both negative ages",
        "negative cat age and second year dog"
    ]
)
def test_get_human_age_with_negative_values(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    """
    Test get_human_age function with negative inputs.
    Expects specific output for negative inputs.

    :param cat_age: The age of the cat in cat years.
    :param dog_age: The age of the dog in dog years.
    :param expected: The expected output for negative inputs.
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


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("fifteen", 15),
        (15, "fifteen"),
        ("fifteen", "fifteen")
    ],
    ids=[
        "string cat age",
        "string dog age",
        "both string ages"
    ]
)
def test_get_human_age_with_invalid_type_values(
        cat_age: int | str,
        dog_age: int | str
) -> None:
    """
    Test the get_human_age function with invalid type inputs.
    This test checks if TypeError is raised when non-integer values
    (specifically strings) are provided as ages.

    :param cat_age: The age of the cat, which should be an integer, but is
                    given as a string in this test.
    :param dog_age: The age of the dog, which should be an integer, but is
                    given as a string in this test.
    """
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
