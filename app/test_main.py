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
        (16, 16, [1, 1]),
        (24, 23, [2, 1]),
        (23, 24, [1, 2]),
        (30, 30, [3, 3]),
        (50, 50, [8, 7]),
        (60, 60, [11, 9]),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int,
                       expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected
