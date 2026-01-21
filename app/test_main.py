import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected", [
        pytest.param(
            0, 0, [0, 0],
            id="0 cat/dog years should be 0 human age"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="under 15 cat/dog years should be 0 human age"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="15 cat/dog years give 1 human year"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="under 24 cat/dog years should be 1 human age"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="24 cat/dog years give 2 human year"
        ),
        pytest.param(
            27, 27, [2, 2],
            id="under 28 cat year and under 29 dog year should be 2 human age"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="28 cat years and 28 dog year give 3/2 human years"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="100 cat/dog years give 21/17 human years"
        ),
        pytest.param(
            -10, -3, [0, 0],
            id="negative cat/dog age give 0 human years"
        )
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: int
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error", [
        pytest.param(
            "12", 1, TypeError,
            id="str value instead of int"
        ),
        pytest.param(
            [], 1, TypeError,
            id="list value instead of int"
        ),
        pytest.param(
            {}, 1, TypeError,
            id="dict value instead of int"
        ),
        pytest.param(
            (), 1, TypeError,
            id="tuple value instead of int"
        )
    ]
)
def test_incorrect_value(
        cat_age: int,
        dog_age: int,
        expected_error: Any
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
