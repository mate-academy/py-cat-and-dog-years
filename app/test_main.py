from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, converted_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_human_age_converted_from_cat_and_dog(
        cat_age: int,
        dog_age: int,
        converted_age: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == converted_age


def test_correct_cat_age_type(cat_age: int) -> None:
    if not isinstance(cat_age, int):
        assert TypeError, f"{cat_age} must be integer type"


def test_correct_dog_age_type(dog_age: int) -> None:
    if not isinstance(dog_age, int):
        assert TypeError, f"{dog_age} must be integer type"
