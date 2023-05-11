import pytest
from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            -4,
            -2,
            [0, 0],
            id="Correct if arguments are negative"
        ),
        pytest.param(
            0,
            0,
            [0, 0],
            id="Correct if arguments are equal 0"
        ),
        pytest.param(
            13,
            14,
            [0, 0],
            id="Correct if age under 15"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="Correct if age equal 15"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="Correct if age above 15 and under 24"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="Correct if age equal 24"
        ),
        pytest.param(
            27,
            26,
            [2, 2],
            id="Correct if age above 24"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="Correct when age start counting differently "
        )
    ]
)
def test_get_human_age_with_correct_value(
        cat_age: int,
        dog_age: int,
        expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param(
            [2],
            5,
            TypeError,
            id="Raise TypeError if age is not integer",
        ),
        pytest.param(
            34,
            "4",
            TypeError,
            id="Raise TypeError if age is not integer",
        )
    ],
)
def test_raising_errors_correctly(cat_age: int,
                                  dog_age: int,
                                  expected_error: Any) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
