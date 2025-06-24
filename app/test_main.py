from typing import List
import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cats_age,dogs_age,expected_human_age",
    [

        pytest.param(0, 0, [0, 0],
                     id="0 cat/dog years should convert into 0 human age."),
        pytest.param(14, 14, [0, 0],
                     id="14 cat/dog years should convert into 0 human age."),
        pytest.param(15, 15, [1, 1],
                     id="15 cat/dog years should convert into 1 human age."),
        pytest.param(23, 23, [1, 1],
                     id="23 cat/dog years should convert into 1 human age."),
        pytest.param(24, 24, [2, 2],
                     id="24 cat/dog years should convert into 2 human age.")

    ]
)
def test_get_human_age(cats_age: int, dogs_age: int,
                       expected_human_age: List[int]) -> None:
    assert get_human_age(cats_age, dogs_age) == expected_human_age
