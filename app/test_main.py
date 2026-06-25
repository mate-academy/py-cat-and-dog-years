import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_array",
    [
        pytest.param(
            0, 0, [0, 0],
            id="test should return zero when age is zero"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="test should add human year for first 15 animal's years"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="test should add second human year for next 9 animal's years past 15th"  # noqa: E501
        ),
        pytest.param(
            28, 28, [3, 2],
            id="test should convert age for each animal accordingly"
        ),
        pytest.param(
            10_000, 10_000, [2496, 1997],
            id="test should convert large age numbers"
        )
    ]
)
def test_should_convert_age_correctly(
    cat_age: int,
    dog_age: int,
    expected_array: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_array


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_exception",
    [
        pytest.param(
            -1, -1, ValueError,
            id="test should raise exception when age is negative"
        ),
        pytest.param(
            None, "", TypeError,
            id="test should raise exception when no age is given"
        ),
        pytest.param(
            3.5, "1", TypeError,
            id="test should raise exception when input is not an integer"
        )
    ]
)
def test_should_raise_exception_if_arguments_are_invalid(
        cat_age: Any,
        dog_age: Any,
        expected_exception: type[Exception]
) -> None:
    with pytest.raises(expected_exception):
        get_human_age(cat_age, dog_age)
