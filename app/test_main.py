import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_years",
    [
        (
            0, 0, [0, 0]
        ),
        (
            14, 14, [0, 0]
        ),
        (
            15, 15, [1, 1]
        ),
        (
            23, 23, [1, 1]
        ),
        (
            24, 24, [2, 2]
        ),
        (
            27, 27, [2, 2]
        ),
        (
            28, 28, [3, 2]
        ),
        (
            100, 100, [21, 17]
        )
    ]
)
def test_get_correct_human_age(cat_age: int,
                               dog_age: int,
                               expected_years: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_years


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_years",
    [
        (
            -1, 8, [0, 0]
        ),
        (
            2, -10, [0, 0]
        ),
        (
            -2, -25, [0, 0]
        )
    ]
)
def test_negative_age(cat_age: int,
                      dog_age: int,
                      expected_years: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_years
