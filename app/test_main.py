import pytest
from app.main import get_human_age  # припустимо, функція знаходиться в main.py


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),          # Вік 0 років для кота та собаки
        (14, 14, [0, 0]),        # Коти та собаки на першому році життя
        (15, 15, [1, 1]),        # Перше людське значення для кота та собаки
        (23, 23, [1, 1]),        # Перший та другий рік
        (24, 24, [2, 2]),        # Початок третього року життя
        (27, 27, [2, 2]),        # Коти та собаки на 27-му році
        (28, 28, [3, 2]),        # Коти та собаки на 28-му році
        (100, 100, [21, 17]),    # Вік 100 років
    ]
)
def test_get_human_age_valid(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_get_human_age_negative() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, 10)
    with pytest.raises(ValueError):
        get_human_age(10, -5)


def test_get_human_age_large_values() -> None:
    assert get_human_age(10**6, 10**6) == [249996, 199997]


@pytest.mark.parametrize(
    "cat_age, dog_age", [
        ("15", 15),
        (15, "15"),
        (None, 15),
        (15, None),
        ([15], 15),
        (15, {"age": 15}),
    ]
)
def test_get_human_age_invalid_types(cat_age: object, dog_age: object) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
