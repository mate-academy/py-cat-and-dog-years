import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age_returns_correct_values(
        cat_age: int,
        dog_age: int,
        expected: list[int, int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected, (
        f"Expected human age for cat age {cat_age}"
        f" and dog age {dog_age} should be {expected},"
        f"but got {get_human_age(cat_age, dog_age)}."
    )
