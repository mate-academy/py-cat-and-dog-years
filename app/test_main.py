import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years,dog_years,human_years",
    [
        (0, 0, [0, 0]),
        (14.3, 14.8, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (1216, 1514, [300, 300]),
        (-4, -15, [0, 0])
    ],
    ids=[
        "should convert to 0 if animal years are less than 15",
        ("should convert to 0 if animal years are less than 15 "
         "and numbers are float"),
        "should convert to 1 if animal years are 15",
        "should convert to 1 if animal years are between 15 and 23 inclusive",
        "should convert to 2 if animal years are 24",
        "should convert to 3 and 2 if animal years are 28",
        "should return the answer if animal years are too big",
        "should convert to 0 if animal years are negative"
    ]
)
def test_convert_animal_age_to_human_age(
        cat_years: int, dog_years: int, human_years: list[int]
) -> None:
    assert get_human_age(cat_years, dog_years) == human_years


@pytest.mark.parametrize(
    "cat_years,dog_years",
    [
        ("one", 5),
        (8, [3]),
    ],
    ids=[
        "should raise error if animal year type is string",
        "should raise error if animal year type is list",
    ]
)
def test_raise_errors_correctly(
        cat_years: int, dog_years: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_years, dog_years)
