import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (23, 22, [1, 1]),
        (28, 28, [3, 2]),
        (1000, 1000, [246, 197]),
        (-1, -1, [0, 0]),
    ],
    ids=["Both ages are zero",
         "Both ages are less than the first_year",
         "Both ages are greater than the second_year",
         "Dog input greater, ages are equal",
         "Cat input greater, ages are equal",
         "Different ages between dogs and cats"
         "Dog age greater than cat age",
         "Large numbers", "Negative ages"]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("cat", "dog"),
        (None, None),
        ({}, []),
    ],
    ids=["String inputs",
         "None inputs",
         "Unsupported types"]
)
def test_get_human_age_type_error(cat_age, dog_age) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
