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
    "first_year,second_year,each_year_cat,each_year_dog",
    [
        (14, 9, 4, 5),
        (15.1, 9, 4, 5),
        (15, 8, 4, 5),
        (15, 9.1, 4, 5),
        (15, 9, 3, 4),
        (15, 9, 4.1, 5.1),
    ],
    ids=[
        "14 cat/dog years should convert into 0 human age.",
        "15 cat/dog years should convert into 1 human age.",
        "23 cat/dog years should convert into 1 human age.",
        "24 cat/dog years should convert into 2 human age.",
        "27/28 cat/dog years should convert into 2 human age.",
        "28/29 cat/dog years should convert into 3 human age.",
    ]
)
def test_ages(monkeypatch, first_year, second_year, each_year_cat, each_year_dog):

    def mock_get_human_age(cat_age, dog_age):
        cat_to_human = convert_to_human(cat_age, first_year, second_year, each_year_cat)
        dog_to_human = convert_to_human(dog_age, first_year, second_year, each_year_dog)
        return [cat_to_human, dog_to_human]

    monkeypatch.setattr(main, "get_human_age", mock_get_human_age)

    test_result = pytest.main(["app/test_main.py"])
    print(f"test_result{test_result}")
    assert test_result.value == 1
