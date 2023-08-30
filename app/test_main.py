import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(
            0, 0, [0, 0],
            id="0 cat/dog years convert into 0 human years"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="14 cat/dog years convert into 0 human years"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="15 cat/dog years convert into 1 human years"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="23 cat/dog years convert into 1 human years"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="24 cat/dog years convert into 2 human years"
        ),
        pytest.param(
            27, 28, [2, 2],
            id="27/28 cat/dog years convert into 2 human years"
        ),
        pytest.param(
            28, 29, [3, 3],
            id="28/29 cat/dog years convert into 3 human years"
        ),
        pytest.param(
            -1, -1, [0, 0],
            id="-1/-1 cat/dog years convert into 0 human years"
        )
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param(
            "0", "0", TypeError,
            id="invalid type should raise TypeError"
        )
    ]
)
def raising_error(
        cat_age: int,
        dog_age: int,
        expected_error: Any):
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
