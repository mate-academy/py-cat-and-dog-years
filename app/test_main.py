from typing import List
import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cats_age,dogs_age,expected_human_age",
    [

        pytest.param(0, 0, [0, 0], id="Zeros case"),
        pytest.param(14, 14, [0, 0], id="0 humans year case"),
        pytest.param(15, 15, [1, 1], id="1 year case"),
        pytest.param(24, 24, [2, 2], id="2 years case")

    ]
)
def test_get_human_age(cats_age: int, dogs_age: int,
                       expected_human_age: List[int]) -> None:
    assert get_human_age(cats_age, dogs_age) == expected_human_age
