from typing import Any

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (14, 14, [0, 0]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (-1, -1, [0, 0]),
        (17, 17, [1, 1]),
        (100, 100, [21, 17])
    ],
    ids=[
        "Age less than 15 should return [0, 0]",
        "Age equals to 23 return [1, 1]",
        "When age 24 should return [2, 2]",
        "Negative ages should return [0, 0]",
        "When age equals to 15 and less than 24 should return [1, 1]",
        "When age 100 should return 21 for cat and 17 for dog"
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: list,
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("five", "five"),
        (None, None),
    ],
    ids=[
        "Raise TypeError when input is str",
        "Raise TypeError when input is None"
    ]
)
def test_human_age_for_invalid_input(
        cat_age: Any,
        dog_age: Any,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
