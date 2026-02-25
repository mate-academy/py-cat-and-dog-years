import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        # examples from task
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),

        # boundary tests — cat
        (16, 0, [1, 0]),
        (24, 0, [2, 0]),
        (25, 0, [2, 0]),
        (28, 0, [3, 0]),
        (29, 0, [3, 0]),

        # boundary tests — dog
        (0, 16, [0, 1]),
        (0, 24, [0, 2]),
        (0, 25, [0, 2]),
        (0, 29, [0, 3]),
        (0, 30, [0, 3]),

        # mixed values
        (40, 50, [6, 7]),
        (50, 40, [8, 5]),
    ],
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
