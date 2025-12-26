import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="should return zeros"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="should return zeros"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="should return ones"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="should return ones"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="should return twos"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="should return 3 for cat and 2 for dog"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="should return 21 for cat and 17 for dog"
        ),
        pytest.param(
            -10,
            -10,
            [0, 0],
            id="should return zeros when inputs less the then zero"
        ),
    ]
)
def test_get_human_age_works_correctly(
    cat_age: int,
    dog_age: int,
    result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize("input1, input2", [
    ("10", "10"),
])
def test_get_human_age_raises_exception(input1: Any, input2: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(input1, input2)
