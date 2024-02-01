import pytest
from typing import List
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, expected",
    [
        pytest.param(
            0, 0, [0, 0],
            id="Test for 0 cat/dog years should return [0, 0]"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="Test for 14 cat/dog years should return [0, 0]"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="Test for 15 cat/dog years should return [1, 1]"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="Test for 23 cat/dog years should return [1, 1]"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="Test for 24 cat/dog years should return [2, 2]"
        ),
        pytest.param(
            27, 27, [2, 2],
            id="Test for 27 cat/dog years should return [2, 2]"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="Test for 28 cat/dog years should return [3, 2]"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="Test for 100 years should return [21, 17]"
        ),
        pytest.param(
            -1, -1, [0, 0],
            id="Test for negative cat/dog years should return[0, 0]"
        )
    ]
)
def test_get_human_age(
        cat_years: int,
        dog_years: int,
        expected: List[int],
) -> None:
    assert get_human_age(cat_years, dog_years) == expected


def test_human_age_incorrect_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("cat", "dog")
