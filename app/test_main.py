import pytest

from app import main


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (0, 5, [0, 0]),
        (3, 0, [0, 0]),
        (5, 5, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (1000, 1000, [246, 197])
    ]
)
def test_get_human_age_pet_positive(cat_age: int,
                                    dog_age: int,
                                    expected: list) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (28, 28, [3, 2]),
        (17, 29, [1, 3]),
        (29, 6, [3, 0]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age_pet_independent(cat_age: int,
                                       dog_age: int,
                                       expected: list) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 3),
        (5, -20),
        (-7, -8),
    ]
)
def test_get_human_age_raises_value_error(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        main.get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("14", 15),
        (15, 1.2),
        ((40, 30), 2),
        (4, None),
        ([9, 4, 5.3], 3),
        (3, [2, 5, 7.6])
    ]
)
def test_get_human_age_raises_type_error(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)
