import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result_list_in_human_years",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
        (-10, -1, [0, 0]),
    ],
    ids=[
        "zero_ages",
        "almost_one_year",
        "one_year",
        "almost_two_years",
        "two_years",
        "cat_3_dog_2",
        "cat_3_dog_3",
        "large_ages",
        "negative_are_zeroed",
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       result_list_in_human_years: list) -> None:
    assert get_human_age(cat_age, dog_age) == result_list_in_human_years


@pytest.mark.parametrize(
    "cat_age_list, dog_age_str, error",
    [
        (-10, "s", TypeError),
        ([], 10, TypeError),
    ]
)
def test_get_human_age_raises_error(cat_age_list: list,
                                    dog_age_str: str,
                                    error: Exception) -> None:
    with pytest.raises(error):
        get_human_age(cat_age_list, dog_age_str)
