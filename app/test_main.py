from typing import List
import pytest
from app.main import get_human_age

@pytest.mark.parametrize(
    "cat_age, dog_age, expected", [
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
def test_get_human_age_examples(
    cat_age: int, dog_age: int, expected: List[int]
) -> None:
    """Перевірка прикладів із завдання."""
    result: List[int] = get_human_age(cat_age, dog_age)
    assert result == expected

@pytest.mark.parametrize(
    "cat_age, dog_age", [
        (15, 14),
        (14, 15),
        (23, 22),
        (22, 23),
        (28, 27),
        (27, 28),
    ]
)
def test_get_human_age_mixed(
    cat_age: int, dog_age: int
) -> None:
    """
    Перевірка для різних значень, що:
    - повернутий результат є списком з двох елементів;
    - обидва елементи є цілими числами.
    """
    result: List[int] = get_human_age(cat_age, dog_age)
    assert isinstance(result, list)
    assert len(result) == 2
    assert isinstance(result[0], int)
    assert isinstance(result[1], int)
