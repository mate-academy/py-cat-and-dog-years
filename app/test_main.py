import pytest
from app.main import convert_to_human, get_human_age
from typing import Type


@pytest.mark.parametrize("animal_age, first_year, second_year, "
                         "each_year, expected", [
                             (0, 15, 9, 4, 0),
                             (14, 15, 9, 4, 0),
                             (15, 15, 9, 4, 1),
                             (23, 15, 9, 4, 1),
                             (24, 15, 9, 4, 2),
                             (26, 15, 9, 4, 2),
                         ])
def test_convert_to_human(
        animal_age: int,
        first_year: int,
        second_year: int,
        each_year: int,
        expected: int
) -> None:
    result = convert_to_human(
        animal_age,
        first_year,
        second_year,
        each_year
    )
    assert result == expected


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
])
def test_get_human_age_valid_inputs(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    ("-5", 10, ValueError),
    ((5, 5), -10, ValueError),
    ([5.5], 10, ValueError),
])
def test_get_human_age_invalid_inputs(
    cat_age: str or tuple or list,
    dog_age: str or tuple or list,
    expected: Type[Exception]
) -> None:
    with pytest.raises(expected):
        get_human_age(cat_age, dog_age)
