from app.main import get_human_age
import pytest


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
        (-1, -1, [0, 0]),
        (10000, 10000, [2496, 1997]),
    ]
)
def test_get_human_age_valid_input(
        cat_age: int,
        dog_age: int,
        expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("ten", 10),
        (10, "twenty"),
        (None, 20),
        ([10], 20),
        (10, {20: "twenty"}),
    ]
)
def test_get_human_age_invalid_input(cat_age: object, dog_age: object) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
