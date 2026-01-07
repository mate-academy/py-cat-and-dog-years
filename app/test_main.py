import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),           # Менше 15 років
        (14, 14, [0, 0]),         # Граничне значення перед 15
        (15, 15, [1, 1]),         # Перший поріг (15 років = 1 людський)
        (23, 23, [1, 1]),         # Граничне значення перед 24
        (24, 24, [2, 2]),         # Другий поріг (15 + 9 = 2 людських)
        (27, 27, [2, 2]),         # Все ще 2 роки (24 + 3)
        (28, 28, [3, 2]),         # Кіт: 24+4 (+1 рік), Собака: 24+4 (ще не +1)
        (29, 29, [3, 3]),         # Собака: 24+5 (+1 рік)
        (100, 100, [21, 17]),     # Великі числа з прикладу
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: int) -> None:
    assert get_human_age(cat_age, dog_age) == expected
