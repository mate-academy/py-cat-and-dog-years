import pytest
from typing import List  # <-- ДОДАНО: імпортуємо List для сумісності
from app.main import get_human_age


EXAMPLES = [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
]


@pytest.mark.parametrize(
    "cat_age, dog_age, expected", EXAMPLES
)
def test_get_human_age_examples(
    cat_age: int, dog_age: int, expected: List[int]  # <-- ВИПРАВЛЕНО: list -> List
) -> None:
    """
    Перевіряє функцію get_human_age на всіх прикладах
    з опису завдання.
    """
    assert get_human_age(cat_age, dog_age) == expected


def test_cat_age_boundaries() -> None:
    """
    Окремо перевіряє "граничні" точки зміни віку для кота.
    """
    assert get_human_age(14, 0)[0] == 0
    assert get_human_age(15, 0)[0] == 1
    assert get_human_age(23, 0)[0] == 1
    assert get_human_age(24, 0)[0] == 2
    assert get_human_age(27, 0)[0] == 2
    assert get_human_age(28, 0)[0] == 3
    assert get_human_age(31, 0)[0] == 3
    assert get_human_age(32, 0)[0] == 4


def test_dog_age_boundaries() -> None:
    """
    Окремо перевіряє "граничні" точки зміни віку для собаки.
    """
    assert get_human_age(0, 14)[1] == 0
    assert get_human_age(0, 15)[1] == 1
    assert get_human_age(0, 23)[1] == 1
    assert get_human_age(0, 24)[1] == 2
    assert get_human_age(0, 28)[1] == 2
    assert get_human_age(0, 29)[1] == 3
    assert get_human_age(0, 33)[1] == 3
    assert get_human_age(0, 34)[1] == 4
