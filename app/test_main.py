import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (24, 24, [2, 2]),
        (14, 14, [0, 0]),
        (28, 28, [3, 2]),
        (30, 30, [3, 3]),
        (35, 18, [4, 1]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (25, 25, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3])
    ]
)
def test_age_cat_and_dog(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (-1, 10),
        (10, -1),
        (-1, -1)
    ]
)
def test_value_error(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)
