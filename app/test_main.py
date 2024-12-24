import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "Both cat and dog age 0 -> [0, 0]",
        "Both cat and dog age 14 -> [0, 0]",
        "Both cat and dog age 15 -> [1, 1]",
        "Both cat and dog age 23 -> [1, 1]",
        "Both cat and dog age 24 -> [2, 2]",
        "Both cat and dog age 27 -> [2, 2]",
        "Both cat and dog age 28 -> [3, 2]",
        "Both cat and dog age 100 -> [21, 17]"
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
