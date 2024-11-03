from app.main import get_human_age

import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_works_correctly(
        cat_age: int,
        dog_age: int,
        result: list[int]
) -> None:
    assert (get_human_age(cat_age, dog_age) == result), \
        f"The conversion of {cat_age} and {dog_age} must be equal to {result}"
