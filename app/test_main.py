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
        (-10, -2, ValueError),
        (1005, 1001, ValueError),
    ],
    ids=[
        "0/0 cat/dog years should be convert to [0, 0]",
        "16/16 cat/dog years should be convert to [1, 1]",
        "25/28 cat/dog years should be convert to [2, 2]",
        "14/14 cat/dog years should be convert to [0, 0]",
        "44/48 cat/dog years should be convert to [7, 6]",
        "should return a ValueError with negative numbers",
        "should return a ValueError with numbers larger 10000",
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected_human_age: list[int, int],
) -> None:
    if (cat_age < 0 or cat_age > 1000) or (dog_age < 0 or dog_age > 1000):
        with pytest.raises(ValueError):
            get_human_age(cat_age, dog_age)
    else:
        assert get_human_age(cat_age, dog_age) == expected_human_age
