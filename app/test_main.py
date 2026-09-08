from typing import Any
import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        # Менше 15 років -> 0
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 0, [0, 0]),
        (0, 14, [0, 0]),
        (14, 14, [0, 0]),
        # 15 років -> 1 рік
        (15, 0, [1, 0]),
        (0, 15, [0, 1]),
        (15, 15, [1, 1]),
        # 23 роки -> все ще 1 рік
        (23, 0, [1, 0]),
        (0, 23, [0, 1]),
        (23, 23, [1, 1]),
        # 24 роки -> 2 роки
        (24, 0, [2, 0]),
        (0, 24, [0, 2]),
        (24, 24, [2, 2]),
        # Рубежі для кота (27 -> 2, 28 -> 3) і собаки (28 -> 2, 29 -> 3)
        (27, 27, [2, 2]),
        (28, 27, [3, 2]),
        (27, 28, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        # Великі значення
        (100, 100, [21, 17]),
        (1000, 1000, [246, 197]),
        (10000, 10000, [2496, 1997]),
    ],
)
def test_get_human_age(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        (None, 15),
        (15, None),
        (15.0, 15),
        (15, 15.0),
        (True, 15),
        (15, False),
    ],
)
def test_get_human_age_raises_type_error(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
