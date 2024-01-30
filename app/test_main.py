import pytest
from typing import List

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (150, 150, [33, 27]),
        (
            int(13e29),
            int(7e14),
            [324999999999999985351879819260, 139999999999997]
        ),
        (5, 10, [0, 0]),
        (0, 0, [0, 0]),
        (-1, -5, [0, 0]),
        (14, 14, [0, 0]),
        (28, 28, [3, 2]),
        (27, 33, [2, 3])
    ],
    ids=[
        "Should return value without extra years",
        "Should return value without extra years",
        "Should return value with extra years",
        "Should return correct result for large numbers",
        "Should return zero when age is too small",
        "Should return zero if age is zero",
        "Should return zero if age is negative",
        "Should return zero when age is too small",
        "Should correct value with or without extra years",
        "Should correct value with or without extra years"
    ]
)
def test_should_return_correct_result(
        cat_age: int,
        dog_age: int,
        expected_result: List[int]
) -> None:

    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        ([1, 2, 3], 45, pytest.raises(TypeError)),
        ("String", "otherstring", pytest.raises(TypeError)),
        (134, {"key": 34}, pytest.raises(TypeError)),
    ],
    ids=[
        "Should raise TypeError if age is list",
        "Should raise TypeError if age is string",
        "Should raise TypeError if age is dict",
    ]
)
def test_division(cat_age: int, dog_age: int, expected: Exception) -> None:
    with expected:
        get_human_age(cat_age, dog_age)
