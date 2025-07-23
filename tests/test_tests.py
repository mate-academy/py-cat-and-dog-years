import pytest
from app import main

def convert_to_human(age, first, second, each):
    if age < first:
        return 0
    elif age < first + second:
        return 1
    else:
        return 2 + int((age - first - second) // each)

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
        "15.1 cat/dog years should convert into 1 human age.",
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

    # Test przykładowych wartości
    assert main.get_human_age(14, 14) == [
        convert_to_human(14, first_year, second_year, each_year_cat),
        convert_to_human(14, first_year, second_year, each_year_dog),
    ]
    assert main.get_human_age(15, 15) == [
        convert_to_human(15, first_year, second_year, each_year_cat),
        convert_to_human(15, first_year, second_year, each_year_dog),
    ]
    assert main.get_human_age(24, 24) == [
        convert_to_human(24, first_year, second_year, each_year_cat),
        convert_to_human(24, first_year, second_year, each_year_dog),
    ]
