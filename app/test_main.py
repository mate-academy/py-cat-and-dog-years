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
        (-1, -5, [0, 0]),  # Кейс с отрицательными числами (out-of-range)
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_should_raise_error_with_non_integer_arguments() -> None:
    # Проверка на некорректные типы данных (строки вместо чисел)
    with pytest.raises(TypeError):
        get_human_age("20", 20)

    with pytest.raises(TypeError):
        get_human_age(20, [20])
