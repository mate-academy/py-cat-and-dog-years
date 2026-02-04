from app.main import get_human_age
import pytest


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
        (10000000, 10000000, [2499994, 1999995])
    ]
)
def test_should_convert_cat_and_dog_years_to_human_age(
        cat_age: int,
        dog_age: int,
        expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected

@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -1),
        (5, -5),
    ]
)

def test_should_raise_exception_for_negative_age(
        cat_age: int,
        dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (None, 10),
        (10, None),
        ('10', 5),
        (5, '10'),
        (5, 10.5),
        (10.5, 5),
    ],
)

def test_should_raise_type_error_for_invalid_age(
        cat_age: int,
        dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
