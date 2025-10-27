import pytest
from app.main import get_human_age  # Припускаємо, що функція тут


# Збираємо всі приклади з опису завдання
EXAMPLES = [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),    # Ключовий випадок, де вік відрізняється
    (100, 100, [21, 17]),  # Складний випадок
]


@pytest.mark.parametrize(
    "cat_age, dog_age, expected", EXAMPLES
)
def test_get_human_age_examples(
    cat_age: int, dog_age: int, expected: list[int]
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
    assert get_human_age(14, 0)[0] == 0  # До 1-го року
    assert get_human_age(15, 0)[0] == 1  # Початок 1-го року
    assert get_human_age(23, 0)[0] == 1  # Кінець 1-го року
    assert get_human_age(24, 0)[0] == 2  # Початок 2-го року
    assert get_human_age(27, 0)[0] == 2  # Кінець 2-го року
    assert get_human_age(28, 0)[0] == 3  # Початок 3-го року (2 + (28-24)//4 = 3)
    assert get_human_age(31, 0)[0] == 3  # До 4-го року
    assert get_human_age(32, 0)[0] == 4  # Початок 4-го року (2 + (32-24)//4 = 4)


def test_dog_age_boundaries() -> None:
    """
    Окремо перевіряє "граничні" точки зміни віку для собаки.
    """
    assert get_human_age(0, 14)[1] ==
