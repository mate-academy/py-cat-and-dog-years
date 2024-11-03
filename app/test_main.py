import pytest
from app import main


def convert_to_human(animal_age: int,
                     first_year: int,
                     second_year: int,
                     each_year: int) -> int:
    if animal_age < first_year:
        return 0
    elif animal_age < first_year + second_year:
        return 1
    else:
        return 2 + (animal_age - first_year - second_year) // each_year


@pytest.mark.parametrize(
    "first_year,"
    "second_year,"
    "each_year_cat,"
    "each_year_dog,"
    "cat_age,dog_age,"
    "expected_human_ages",
    [
        (15, 9, 4, 5, 14, 14, [0, 0]),
        (15, 9, 4, 5, 15, 15, [1, 1]),
        (15, 9, 4, 5, 23, 23, [1, 1]),
        (15, 9, 4, 5, 24, 24, [2, 2]),
        (15, 9, 4, 5, 27, 27, [2, 2]),
        (15, 9, 4, 5, 28, 28, [3, 3]),
        (15, 9, 4, 5, 29, 29, [3, 3]),
    ],
    ids=[
        "14 cat and dog years should convert into 0 human age.",
        "15 cat and dog years should convert into 1 human age.",
        "23 cat and dog years should convert into 1 human age.",
        "24 cat and dog years should convert into 2 human age.",
        "27 cat years should convert into 2 human age.",
        "28 cat years should convert into 3 human age.",
        "29 dog years should convert into 3 human age.",
    ]
)
def test_ages(monkeypatch: pytest.MonkeyPatch,
              first_year: int, second_year: int,
              each_year_cat: int, each_year_dog: int,
              cat_age: int, dog_age: int,
              expected_human_ages: list[int]) -> None:
    def mock_get_human_age(cat_age: int, dog_age: int) -> list[int]:
        cat_to_human = convert_to_human(cat_age, first_year,
                                        second_year, each_year_cat)
        dog_to_human = convert_to_human(dog_age, first_year,
                                        second_year, each_year_dog)
        return [cat_to_human, dog_to_human]

    monkeypatch.setattr(main, "get_human_age", mock_get_human_age)

    result = main.get_human_age(cat_age, dog_age)
    assert result == expected_human_ages,\
        f"Expected {expected_human_ages} but got {result}"
