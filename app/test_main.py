from typing import List
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
def test_get_human_age_returns_correct_values(
    cat_age: int, dog_age: int, expected: List[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [(-1, 10), (10, -5), (-3, -7)],
)
def test_get_human_age_with_negative_values(
    cat_age: int, dog_age: int
) -> None:
    """Перевіряє, що від’ємний вік дає 0 років для обох."""
    result = get_human_age(cat_age, dog_age)
    assert result[0] >= 0
    assert result[1] >= 0


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [(15, 14), (23, 22), (28, 27)],
)
def test_cat_and_dog_ages_change_independently(
    cat_age: int, dog_age: int
) -> None:
    """Кіт і пес мають незалежну шкалу віку."""
    cat_human, dog_human = get_human_age(cat_age, dog_age)
    assert isinstance(cat_human, int)
    assert isinstance(dog_human, int)
