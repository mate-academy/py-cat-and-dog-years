import pytest
from app.main import get_human_age


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
    ],
)
def test_get_human_age_valid(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    """Проверка корректных значений."""
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [(-5, 10), (10, -2), (-3, -7)],
)
def test_get_human_age_negative_values(
    cat_age: int, dog_age: int
) -> None:
    result = get_human_age(cat_age, dog_age)
    assert all(isinstance(x, int) and x >= 0 for x in result)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [("10", 10), (15, "15"), ("a", "b")],
)
def test_get_human_age_invalid_types(
    cat_age: object, dog_age: object
) -> None:
    """Проверяем, что при некорректных типах выбрасывается TypeError."""
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
