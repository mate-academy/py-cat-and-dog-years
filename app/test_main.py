import pytest
from app.main import get_human_age


def calculate_result(cat_age: int, dog_age: int) -> list[int]:
    return get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (1, 1, [15, 15]),
        (2, 2, [24, 24]),
        (14, 14, [76, 76]),
        (15, 15, [80, 80]),
        (23, 23, [116, 120]),
        (24, 24, [120, 125]),
        (27, 27, [132, 140]),
        (28, 28, [136, 145]),
        (100, 100, [388, 512])
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
        (0, 10, [0, 64]),
        (10, 0, [52, 0]),
        (0, 0, [0, 0])
    ]
)
def test_age_zero(cat_age: int, dog_age: int, expected: list[int]) -> None:
    result = calculate_result(cat_age, dog_age)
    assert result == expected, f"Expected {expected}, but got {result}"
