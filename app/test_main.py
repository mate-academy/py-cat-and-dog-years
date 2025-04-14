import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (0, 0, [0, 0]),
        (-1, -1, [0, 0]),
        (-5, 10, [0, 0]),
        (10, -7, [0, 0]),
        (-100, -200, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 29, [3, 3]),
        (40, 40, [6, 5]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "cat_0_and_dog_0_years",
        "both negative",
        "negative cat age",
        "negative dog age",
        "very negative values",
        "cat_14_and_dog_14_years",
        "cat_15_and_dog_15_years",
        "cat_23_and_dog_23_years",
        "cat_24_and_dog_24_years",
        "cat_28_and_dog_29_years",
        "cat_40_and_dog_40_years",
        "cat_100_and_dog_100_years",
    ],
)
def test_get_human_age_returns_correct_values(cat_age: int, dog_age: int, expected_result: list):
    result = get_human_age(cat_age, dog_age)
    assert result == expected_result
    assert isinstance(result, list)
    assert all(isinstance(x, int) for x in result)
    assert len(result) == 2


