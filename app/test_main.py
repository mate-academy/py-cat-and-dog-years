import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (-2, 28, [0, 2]),
        (-2, -5, [0, 0]),
        (-2, -28, [0, 0]),
        (0, -28, [0, 0]),
        (0, 0, [0, 0]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age_with_negative_numbers_and_zero(cat_age: int, dog_age: int, result: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("28", 100),
        ([1], 100),
        ([], 100),
        ({}, 100),
    ]
)
def test_type_error(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
