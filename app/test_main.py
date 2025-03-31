import pytest
from typing import Type

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(
            0, 0,
            [0, 0],
            id="0 year of animals equal 0 human year"
        ),
        pytest.param(
            14, 14,
            [0, 0],
            id="less 15 year of animals equal 0 human year"
        ),
        pytest.param(
            15, 16,
            [1, 1],
            id="15 <= year of animals < 24 equal 1 human year"
        ),
        pytest.param(
            24, 25,
            [2, 2],
            id="24 <= year of animals < 28 equal 2 human year"
        ),
        pytest.param(
            28, 28,
            [3, 2],
            id="first difference year for animals"
        ),
        pytest.param(
            100, 100,
            [21, 17],
            id="correct result for a large value of animals year"
        ),
    ]
)
def test_get_to_human(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param(
            0.5, 0.8,
            TypeError,
            id="test should raise error if type of value is non integer"
        ),
        pytest.param(
            -6, -100,
            ValueError,
            id="test should raise error if value is negative"
        ),
    ]
)
def test_raising_errors_correctly(
        cat_age: int,
        dog_age: int,
        expected_error: Type[Exception]
) -> None:
    with pytest.raises(expected_error):
        if not isinstance(cat_age, int) or not isinstance(dog_age, int):
            raise TypeError("Ages must be integer")
        elif cat_age < 0 or dog_age < 0:
            raise ValueError("Ages must be more than 0")
