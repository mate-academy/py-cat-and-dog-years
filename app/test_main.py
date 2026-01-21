from app.main import get_human_age

import pytest


def test_raise_error_when_incorect_value() -> None:
    with pytest.raises(TypeError):
        get_human_age(0, "0a0")


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="Result equal to [0, 0] when parameters are equal to zero"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="Result equal to [0, 0] when parameters are less then 15"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="Result equal to [1, 1] when both values equal to 15"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="Result equal to [1, 1] when both values equal to 23"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="Result equal to [2, 2] when both values equal to 24"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="Result equal to [3, 2] when both values equal to 28"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="Result equal to [21, 17] when both values equal to 100"
        ),
        pytest.param(
            -1,
            -1,
            [0, 0],
            id="Result are [0, 0], Values should be positive"
        )
    ]
)
def test_get_human_age_correct(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
