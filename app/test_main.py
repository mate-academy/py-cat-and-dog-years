import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 29, [3, 3]),
        (0, 0, [0, 0]),
    ],
)
def test_get_human_age_normal_cases(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (100, 100),
        (50, 60),
    ],
)
def test_get_human_age_large_numbers(cat_age: int, dog_age: int) -> None:
    result = get_human_age(cat_age, dog_age)
    assert all(isinstance(x, int) for x in result)
    assert result[0] >= 0 and result[1] >= 0


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -5),
        (-3, -7),
    ],
)
def test_get_human_age_negative_values(cat_age: int, dog_age: int) -> None:
    result = get_human_age(cat_age, dog_age)
    assert all(x >= 0 for x in result)
