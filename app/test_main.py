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
        (-10, -2, [0, 0]),
        (1005, 1001, [247, 197]),
        ("dog", "cat", [247, 197]),
    ],
    ids=[
        "0/0 cat/dog years should be convert to [0, 0]",
        "16/16 cat/dog years should be convert to [1, 1]",
        "25/28 cat/dog years should be convert to [2, 2]",
        "14/14 cat/dog years should be convert to [0, 0]",
        "44/48 cat/dog years should be convert to [7, 6]",
        "should return a [0, 0] with negative numbers",
        "1005/1001 cat/dog years should be convert to [247, 197]",
        "should return a TypeError with other than 'int' types",
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected_human_age: list[int, int],
) -> None:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
    else:
        assert get_human_age(cat_age, dog_age) == expected_human_age
