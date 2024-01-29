from typing import Type
import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
        (-1, -1, [0, 0]),
    ],
    ids=[
        "0/0 cat/dog years should be convert to [0, 0]",
        "14/14 cat/dog years should be convert to [0, 0]",
        "15/15 cat/dog years should be convert to [1, 1]",
        "23/23 cat/dog years should be convert to [1, 1]",
        "24/24 cat/dog years should be convert to [2, 2]",
        "27/27 cat/dog years should be convert to [2, 2]",
        "28/28 cat/dog years should be convert to [3, 2]",
        "28/29 cat/dog years should be convert to [3, 3]",
        "100/100 cat/dog years should be convert to [21, 17]",
        "Invalid input should return 0",
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected_human_age: list[int, int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        ("14", 14, TypeError),
        (24, "24", TypeError),
        ("28", "29", TypeError),
    ],
    ids=[
        "Cat age should be Integer, not String",
        "Dog age should be Integer, not String",
        "Cat age and Dog age should be Integers, not Strings",
    ],
)
def test_get_human_age_invalid_input_type(
    cat_age: int,
    dog_age: int,
    expected_error: Type[Exception],
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
