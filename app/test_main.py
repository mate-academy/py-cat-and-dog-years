import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "pet_years,result",
    [
        (0, [0, 0]),
        (14, [0, 0]),
        (15, [1, 1]),
        (23, [1, 1]),
        (24, [2, 2]),
        (27, [2, 2])
    ]
)
def test_both_of_functions_should_return_the_same_result(
        pet_years: int, result: list
) -> None:
    assert get_human_age(pet_years, pet_years) == result


@pytest.mark.parametrize(
    "cat_years,dog_years,result",
    [
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_cat_years_should_be_greater_than_dogs_years(
        cat_years: int, dog_years: int, result: list
) -> None:
    assert get_human_age(cat_years, dog_years) == result
