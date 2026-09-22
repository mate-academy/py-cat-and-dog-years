from typing import Any
import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        # Negativos y cero
        (-10, -1, [0, 0]),
        (0, 0, [0, 0]),
        # Límite del primer tramo (14 y 15)
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        # Límite del segundo tramo (23 y 24)
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        # Transiciones específicas de gatos y perros
        (27, 24, [2, 2]),
        (28, 24, [3, 2]),
        (24, 28, [2, 2]),
        (24, 29, [2, 3]),
        # Casos explícitos requeridos por la consigna
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        # Números grandes
        (1000, 1000, [246, 197]),
    ],
)
def test_get_human_age_valid_cases(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        (15.5, 15),
        (15, 15.5),
        (None, 15),
        (15, None),
    ],
)
def test_get_human_age_invalid_types_raise_type_error(
    cat_age: Any, dog_age: Any
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
