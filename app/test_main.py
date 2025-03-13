import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_years",
    [
        (0, 0, [0, 0]),
        (7, 9, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (1200, 1350, [308, 267]),
        (-78, -45, [0, 0])
    ]
)
def test_human_years_calculated_correct(cat_age: int, dog_age:
                                        int, human_years: list) -> None:
    assert (get_human_age(cat_age, dog_age) == human_years)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("gjh", []),
        ("5", 10),
        (5, "10"),
        (None, 5),
        (5, None),
        ([], {}),
        (5.5, 10),
        (10, 3.5),
        (10, "abc")
    ]
)
def test_cat_age_and_dog_age_should_be_int(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
