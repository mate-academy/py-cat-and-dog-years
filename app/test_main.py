import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_year",
    [
        (-1, -10, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (10_000, 5_000, [2_496, 997])
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, human_year: list) -> None:
    if not isinstance(cat_age, int):
        raise TypeError
    if not isinstance(dog_age, int):
        raise TypeError

    assert get_human_age(cat_age, dog_age) == human_year
