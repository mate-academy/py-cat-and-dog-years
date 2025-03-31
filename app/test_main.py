import pytest

from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (-1, -2, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "cat/dog have negative years.",
        "cat/dog have 0 years.",
        "cat/dog have 14 years.",
        "cat/dog have 15 years.",
        "cat/dog have 23 years.",
        "cat/dog have 24 years.",
        "cat/dog have 27/28 years.",
        "cat/dog have 28/29 years.",
        "cat/dog have 100 years."
    ]
)
def test_get_human_age_results(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        ("14", (34, 55), TypeError),
        ([23], {40: 32}, TypeError)
    ],
    ids=[
        "test if there is no strings and tuples",
        "test if there is no lists and dictionaries"
    ]
)
def test_raising_errors_correctly(
        cat_age: int,
        dog_age: int,
        expected_error: Any
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
