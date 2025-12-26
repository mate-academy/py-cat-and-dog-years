from typing import Type

from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [(0, 0, [0, 0]),
     (-1, 0, [0, 0]),
     (14, 14, [0, 0]),
     (14, -14, [0, 0]),
     (15, 15, [1, 1]),
     (-15, 15, [0, 1]),
     (23, 23, [1, 1]),
     (24, 24, [2, 2]),
     (27, 27, [2, 2]),
     (28, 28, [3, 2]),
     (100, 100, [21, 17]),
     (1000, 1000, [246, 197])]
)
def test_if_return_is_correct(
        cat_age: int,
        dog_age: int,
        expected_result: list) -> None:
    assert expected_result == get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [([], 0, TypeError),
     ([-1], 0, TypeError),
     (14, {14}, TypeError),
     (14, (14, 23), TypeError),
     ([15, 15], 0, TypeError)]
)
def test_raise_errors_correctly(
        cat_age: int,
        dog_age: int,
        expected_error: Type[BaseException]) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
