import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [pytest.param(
        0,
        0,
        [0, 0],
        id="should return zeroes if animal\'s age equal zeroes"
    ),
    pytest.param(
        14,
        14,
        [0, 0],
        id="Both cat and dog age 14 -> [0, 0]"
    ),
    pytest.param(
    15,
        15,
        [1, 1],
        id="Both cat and dog age 15 -> [1, 1]"
    ),
    pytest.param(
    23,
        23,
        [1, 1],
        id="Both cat and dog age 23 -> [1, 1]"
    ),
    pytest.param(
    24,
        24,
        [2, 2],
        id="Both cat and dog age 24 -> [2, 2]"
    ),
    pytest.param(
        27,
        27,
        [2, 2],
        id="Both cat and dog age 27 -> [2, 2]"
    ),
    pytest.param(
    28,
        28,
        [3, 2],
        id="Both cat and dog age 28 -> [3, 2]"
    ),
    pytest.param(
        100,
        100,
        [21, 17],
        id="Both cat and dog age 100 -> [21, 17]"
    )]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
