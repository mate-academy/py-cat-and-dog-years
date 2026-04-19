import pytest
from app import main

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
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "zero_age_reeturn_0",
        "before_1st_year",
        "1st_year_under_15",
        "last_year_before_24",
        "2nd_year_under_24",
        "last_year_before_27",
        "cat_3rd_year_threshold",
        "dog_3rd_year_threshold",
        "large_numbers"
    ]
)
def test_get_human_age_valid_inputs(cat_age, dog_age, expected):
    assert main.get_human_age(cat_age, dog_age) == expected

@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 5),
        (5, -1),
        (-10, -10),
    ]
)
def test_get_human_age_negative_values(cat_age, dog_age):
    assert main.get_human_age(cat_age, dog_age) == [0, 0]

@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("5", 5),
        (5, [5]),
        (None, 5),
    ]
)
def test_get_human_age_wrong_types(cat_age, dog_age):
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)
