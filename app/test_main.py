import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(
            "1",
            5,
            TypeError,
            id="Str can not be declared as age"
        ),
        pytest.param(
            [1],
            5,
            TypeError,
            id="List can not be declared as age"
        ),
        pytest.param(
            None,
            5,
            TypeError,
            id="None can not be declared as age"
        )
    ]
)
def test_if_input_is_correct(
        cat_age: Any,
        dog_age: Any,
        result: TypeError
) -> None:
    with pytest.raises(result):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(
            -5,
            -5,
            [0, 0],
            id="Input can not be negative"
        ),
        pytest.param(
            0,
            0,
            [0, 0],
            id="Should return 0 when animal age is 0"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="Should return 1 when animal age is equal 15"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="Should return 2 when animal age is equal 24"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="Should calculate differently when animal age is 28"
        )
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == result
