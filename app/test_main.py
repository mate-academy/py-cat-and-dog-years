import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (16, 16, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (29, 30, [3, 3]),
        (31, 33, [3, 3]),
        (32, 34, [4, 4]),
        (100, 100, [21, 17]),
        (0, 100, [0, 17]),
        (100, 0, [21, 0]),
        (15, 24, [1, 2]),
        (24, 15, [2, 1]),
        (28, 28, [3, 2]),
    ],
)
def test_get_human_age_converts_each_age_correctly(
    cat_age: int,
    dog_age: int,
    expected: list,
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
