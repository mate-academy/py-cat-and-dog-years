import pytest
from app.main import get_human_age


# Основные кейсы и большие числа
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
        (29, 29, [3, 3]),
        (34, 34, [4, 4]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age(cat_age: int, dog_age: int,
                       expected: list[int]) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected
    # проверка структуры результата
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)


# Границы для котов
@pytest.mark.parametrize(
    "cat_age, expected",
    [
        (14, 0),  # перед порогом
        (15, 1),  # на пороге
        (16, 1),  # сразу после порога
        (23, 1),  # конец второй зоны
        (24, 2),  # второй порог
        (27, 2),  # до первого шага после 24
        (28, 3),  # первый шаг после 24
    ],
)
def test_cat_boundaries(cat_age: int, expected: int) -> None:
    human_cat, _ = get_human_age(cat_age, 0)
    assert human_cat == expected


# Границы для собак
@pytest.mark.parametrize(
    "dog_age, expected",
    [
        (14, 0),
        (15, 1),
        (16, 1),
        (23, 1),
        (24, 2),
        (28, 2),
        (29, 3),
    ],
)
def test_dog_boundaries(dog_age: int, expected: int) -> None:
    _, human_dog = get_human_age(0, dog_age)
    assert human_dog == expected


# Неверные типы, которые реально вызывают TypeError
@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("10", 5),
        (None, 5),
    ],
)
def test_invalid_type_inputs(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -5),
        (-3, -3),
        (3.5, 5),
    ],
)
def test_negative_or_float_inputs(cat_age: int, dog_age: int) -> None:
    result = get_human_age(cat_age, dog_age)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)
