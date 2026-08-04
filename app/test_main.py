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
        (28, 27, [3, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (30, 30, [3, 3]),
    ],
)
def test_get_human_age_valid_cases(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),      # негативний вік кота
        (10, -5),      # негативний вік собаки
        ("ten", 10),   # рядок замість числа
        (10, "five"),  # рядок замість числа
        (10.5, 20),    # float замість int
        (20, 15.7),    # float замість int
    ],
)
def test_get_human_age_invalid_inputs(
        cat_age: object, dog_age: object) -> None:
    with pytest.raises((TypeError, ValueError)):
        get_human_age(cat_age, dog_age)
