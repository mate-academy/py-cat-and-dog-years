import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        # Негативні значення (до 15 років -> 0 людських років)
        (-1, 0, [0, 0]),
        (0, -5, [0, 0]),

        # Порогові значення для перших двох років (15 та 24)
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),

        # Перевірка інтервалів для котів (+4 котячих = +1 людський)
        (27, 24, [2, 2]),
        (28, 24, [3, 2]),
        (31, 24, [3, 2]),
        (32, 24, [4, 2]),

        # Перевірка інтервалів для собак (+5 собачих = +1 людський)
        (24, 28, [2, 2]),
        (24, 29, [2, 3]),
        (24, 33, [2, 3]),
        (24, 34, [2, 4]),

        # Великі значення
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_valid_cases(
    cat_age: int,
    dog_age: int,
    expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("15", 15),
        (15, "dog"),
        (None, 15),
        ([], {}),
    ],
)
def test_get_human_age_raises_type_error(
    cat_age: type,
    dog_age: type
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
