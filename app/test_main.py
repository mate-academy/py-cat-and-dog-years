import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),        # менше першого порогу
        (14, 14, [0, 0]),      # ще не 15
        (15, 15, [1, 1]),      # рівно 15
        (23, 23, [1, 1]),      # перед другим порогом
        (24, 24, [2, 2]),      # рівно 24 (15 + 9)
        (28, 0, [3, 0]),       # кіт: кожні 4 роки
        (0, 29, [0, 3]),       # собака: кожні 5 років
        (100, 100, [21, 17]),  # велике значення
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> bool:
    assert get_human_age(cat_age, dog_age) == expected
