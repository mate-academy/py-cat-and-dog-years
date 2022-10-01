import pytest

from app.main import get_human_age
from typing import List


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        pytest.param(
            0, 0, [0, 0],
            id="Should return 0 if age is equal to 0"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="Should return 0 if age is less than 15"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="Should return 1 if cat's or dog's age 15-23"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="Should return 2 if cat's age 24-27 and dog's age 24-28"
        ),
        pytest.param(
            28, 29, [3, 3],
            id="Should return 3 if cat's age 28-31 and dog's age 29-33"
        ),
    ]
)
def test_convert_cat_and_dog_age_into_human_years(
        cat_age: int,
        dog_age: int,
        human_age: List[int]) -> None:
    assert get_human_age(cat_age, dog_age) == human_age
