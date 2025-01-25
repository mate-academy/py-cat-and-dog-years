import pytest
from app.main import get_human_age


def calculate_result(cat_age: int, dog_age: int) -> list[int]:
    return get_human_age(cat_age, dog_age)


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
        (100, 100, [21, 17])
    ]
)
def test_valid_values(cat_age: int, dog_age: int, expected: list[int]) -> None:
    result = calculate_result(cat_age, dog_age)
    assert result == expected, f"Expected {expected}, but got {result}"


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 5),
        (5, -1),
        (-1, -1)
    ]
)
def test_negative_values(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        calculate_result(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 10, [0, 0]),     # Кіт = 0, собака починається з 1
        (10, 0, [0, 0]),     # Собака = 0, кіт повертає 0
    ]
)
def test_edge_cases(cat_age: int, dog_age: int, expected: list[int]) -> None:
    result = calculate_result(cat_age, dog_age)
    assert result == expected, f"Expected {expected}, but got {result}"
