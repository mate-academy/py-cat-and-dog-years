import pytest
from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,output",
    [
        pytest.param(
            -1,
            -3,
            [0, 0],
            id="arguments should be positive"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="less then 15 years should give 0 human year"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="15-23 years should give 1 human year"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="more than 28 cat years should give not less then 3 human years"
        ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="more than 29 dog years should give not less then 3 human years"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="more than 100 years should give not less then 17 human years"
        )
    ],
)
def test_cats_and_dogs_age(
        cat_age: int,
        dog_age: int,
        output: list
) -> None:
    assert get_human_age(cat_age, dog_age) == output


@pytest.mark.parametrize(
    "cat_age,dog_age,error",
    [
        pytest.param("14", "OK", TypeError, id="arguments should be integers"),
        pytest.param(14.5, [14], TypeError, id="arguments should be integers")
    ]
)
def test_args_type(
        cat_age: Any,
        dog_age: Any,
        error: Any
) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)
