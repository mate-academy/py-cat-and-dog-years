import pytest
from app import main


def convert_to_human(
    animal_age: int,
    first_year: int,
    second_year: int,
    each_year: int
) -> int:
    if animal_age < first_year:
        return 0
    if animal_age < first_year + second_year:
        return 1
    return 2 + (animal_age - first_year - second_year) // each_year


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
    ],
    ids=[
        "0 cat/dog years should convert into 0 human age.",
        "14 cat/dog years should convert into 0 human age.",
        "15 cat/dog years should convert into 1 human age.",
        "23 cat/dog years should convert into 1 human age.",
        "24 cat/dog years should convert into 2 human age.",
        "27 cat/dog years should convert into 2 human age.",
        "28 cat/dog years should convert into 3 human age.",
        "100 cat/dog years should convert into 21 and 17 human age.",
    ]
)
def test_ages(
    cat_age: int,
    dog_age: int,
    expected: list
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected
