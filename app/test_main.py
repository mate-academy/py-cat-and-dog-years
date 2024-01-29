from app.main import get_human_age
from typing import List

import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(5, 10, [0, 0],
                     id="Should return zero when age is too small"),
        pytest.param(0, 0, [0, 0],
                     id="Should return zero if age is zero"),
        pytest.param(-1, -5, [0, 0],
                     id="Should return zero if age is negative"),
        pytest.param(14, 14, [0, 0],
                     id="Should return zero when age is too small"),
    ]
)
def test_should_return_zero(
        cat_age: int,
        dog_age: int,
        expected_result: List[int]
) -> None:

    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(15, 15, [1, 1],
                     id="Should return value without extra years"),
        pytest.param(23, 23, [1, 1],
                     id="Should return value without extra years"),
        pytest.param(150, 150, [33, 27],
                     id="Should return value with extra years"),
        pytest.param(int(13e29), int(7e14),
                     [324999999999999985351879819260, 139999999999997],
                     id="Should return correct result for large numbers")
    ]
)
def test_should_correct_result(
        cat_age: int,
        dog_age: int,
        expected_result: List[int]
) -> None:

    assert get_human_age(cat_age, dog_age) == expected_result


def test_should_raise_correct_exception() -> None:

    with pytest.raises(TypeError):
        get_human_age("some_str", 1)
