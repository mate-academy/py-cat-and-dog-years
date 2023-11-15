import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17])
    ]
)
def test_convert_animal_human_age(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("16", 5),
        (12, "Cat"),
        (78, [9, 0])
    ]
)
def test_incorrect_input_type(
        cat_age: Any,
        dog_age: Any
) -> None:
    with pytest.raises(TypeError):
        assert get_human_age(cat_age, dog_age)
