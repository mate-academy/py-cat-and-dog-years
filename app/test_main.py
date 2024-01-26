from app.main import get_human_age

import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_human_age",
    [
        (0, 0, [0, 0]),
        (16, 16, [1, 1]),
        (25, 28, [2, 2]),
        (14, 14, [0, 0]),
        (44, 48, [7, 6]),
    ],
    ids=[
        "0/0 cat/dog years should be convert to [0, 0]",
        "16/16 cat/dog years should be convert to [1, 1]",
        "25/28 cat/dog years should be convert to [2, 2]",
        "14/14 cat/dog years should be convert to [0, 0]",
        "44/48 cat/dog years should be convert to [7, 6]",
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected_human_age: list[int, int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age
