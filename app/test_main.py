from typing import Type

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (23, 23, [1, 1]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-1, -1, [0, 0])
    ],
    ids=[
        "the result is null if the value is null",
        "values less than 15 don't count",
        "if the value is from 15 to 24, the result is 1",
        "if the value is from 25 to 28, the result is 2",
        "for cat age 28 counts as 3, when for dog it still 2",
        "for cat age 100 counts as 21, when for dog it still 17",
        "if function resive data out of normal range, such as negative numbers"
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        ("1", 1, TypeError),
        (1, "1", TypeError),
        ((), (), TypeError),
        ([], {}, TypeError),
        ([1], (), TypeError)
    ]
)
def test_get_human_age_function_incorrect_type(
        cat_age: int,
        dog_age: int,
        expected_error: Type[Exception]
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
