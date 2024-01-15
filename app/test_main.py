from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_output",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],

    ids=[
        "cat and dog ages equals to 0",
        "cat and dog ages equals to 14",
        "cat and dog ages equals to 15",
        "cat and dog ages equals to 23",
        "cat and dog ages equals to 24",
        "cat and dog ages equals to 27",
        "cat and dog ages equals to 28",
        "cat and dog ages equals to 100"
    ]
)
def test_check_human_age_based_on_cat_and_dog_ages(
        cat_age: int,
        dog_age: int,
        expected_output: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_output
