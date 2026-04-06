from typing import Any

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(
            0, 0, [0, 0],
            id="cat & dog ages = 0"
        ),
        pytest.param(
            14, 15, [0, 1],
            id="cat/dog ages = 14/15"
        ),
        pytest.param(
            24, 23, [2, 1],
            id="cat & dog ages = 24/23"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="cat & dog ages = 28/28"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="cat & dog ages = 100/100"
        ),
        pytest.param(
            -1, -3, [],
            id="should return an empty list"
        ),
    ]
)
def test_get_human_age(cat_age: Any, dog_age: Any, result: Any) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param(
            0.0, 0,
            id="float should raise error"
        ),
        pytest.param(
            0, "",
            id="string should raise error"
        ),
        pytest.param(
            (), {1: "dict"},
            id="tuple & dict should raise error"
        ),
        pytest.param(
            [], {1, 2, 3},
            id="list & set should raise error"
        )
    ]
)
def test_get_human_age_raises_error(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
