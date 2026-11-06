from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (0, 0),
        (14, 14),
    ],
)
def test_animal_age_less_than_15_return_0_human_age(
    cat_age: int, dog_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [0, 0]


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (15, 15),
        (23, 23),
    ],
)
def test_animal_age_from_15_to_23_return_1_human_age(
    cat_age: int, dog_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [1, 1]


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (24, 24, [2, 2]),
        (28, 29, [3, 3]),
        (32, 34, [4, 4]),
        (36, 39, [5, 5]),
    ],
)
def test_animal_age_after_24_adds_1_human_year_for_every_4_cat_and_5_dog_years(
    cat_age: int, dog_age: int, result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result
