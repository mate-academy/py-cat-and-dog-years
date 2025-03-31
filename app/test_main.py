from app.main import get_human_age
import pytest
from typing import List

positive_test_cases = [
    pytest.param(
        0, 0, [0, 0],
        id="Both ages are zero"
    ),
    pytest.param(
        14, 14, [0, 0],
        id="Ages below first threshold of 15"
    ),
    pytest.param(
        15, 15, [1, 1],
        id="Ages exactly at first threshold of 15"
    ),
    pytest.param(
        23, 23, [1, 1],
        id="Ages between first and second threshold"
    ),
    pytest.param(
        24, 24, [2, 2],
        id="Ages at second threshold of 24"
    ),
    pytest.param(
        28, 28, [3, 2],
        id="Progression for cat and dog at age 28"
    ),
    pytest.param(
        100, 100, [21, 17],
        id="Testing with large age values"
    ),
]


@pytest.mark.parametrize("cat_age, dog_age, expected", positive_test_cases)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: List[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
