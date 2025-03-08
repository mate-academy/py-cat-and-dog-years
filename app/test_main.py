import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 17, [0, 1]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: int) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-1, -15, [0, 0]),
        (1000, 1000, [246, 197]),
        (99999, 99999, [24995, 19997])
    ]
)
def test_get_human_age_edge_cases(cat_age: int, dog_age: int,
                                  expected: int) -> None:
    assert get_human_age(cat_age, dog_age) == expected
