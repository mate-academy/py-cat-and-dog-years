import pytest

import app.main


@pytest.mark.parametrize(
    "cat_age, dog_age, expected", [
        pytest.param(
            0, 0, [0, 0],
            id="return zeroes for zero inputs"),
        pytest.param(
            14, 14, [0, 0],
            id="return zeroes just before 15"),
        pytest.param(
            15, 15, [1, 1],
            id="return one at 15"),
        pytest.param(
            23, 23, [1, 1],
            id="return one just before 24"),
        pytest.param(
            24, 24, [2, 2],
            id="return two at 24"),
        pytest.param(
            28, 24, [3, 2],
            id="cat_step_increase_at_28"),
        pytest.param(
            24, 29, [2, 3],
            id="dog_step_increase_at_29"),
        pytest.param(
            100, 100, [21, 17],
            id="calculate correctly for large numbers")
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert app.main.get_human_age(cat_age, dog_age) == expected
