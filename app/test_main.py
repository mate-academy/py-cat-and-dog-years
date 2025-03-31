from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "test_zero_age",
        "test_less_than_first_year",
        "test_exactly_first_year",
        "test_between_first_and_second_year",
        "test_exactly_second_year",
        "test_after_second_year",
        "test_different_results",
        "test_large_numbers",
    ]
)
def test_animal_age(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result
