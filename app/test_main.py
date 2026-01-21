import pytest
from typing import Type
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-13, -13, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "Should return 0 if animal_age < 0",
        "Should return 0 if animal_age is 0",
        "Should return 0 if animal_age < first_year value"
        "Should return 1 if animal_age >= first_year < second",
        "Should return 2 if animal_age >= second_year < second + first",
        "Should return 3 if animal age >= 28 < second + first + each",
        "Should return value more than 3 according to convert_to_human func",
        "why I need this string here?"

    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, exception",
    [
        ("not int", "not int", TypeError),
        ("not int", 25, TypeError),
        (23, "not int", TypeError)
    ],
    ids=[
        "Expect TypeError if both parameters is not int",
        "Expect TypeError if one of parameters is not int",
        "Expect TypeError if one of parameters is not int"
    ]
)
def test_check_for_valid_value(
        cat_age: int,
        dog_age: int,
        exception: Type[Exception]
) -> None:
    with pytest.raises(exception):
        get_human_age(cat_age, dog_age)
