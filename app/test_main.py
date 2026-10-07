from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        # Отрицательные значения
        (-1, -1, [0, 0]),
        (-10, -15, [0, 0]),
        # Граничные значения и ноль
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("15", 15),
        (15, "15"),
        ("15", "15"),
        (15.5, 15),
        (15, [15]),
    ],
)
def test_get_human_age_raises_type_error(
    cat_age: int, dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
