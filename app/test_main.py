import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_year,dog_year,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_correct_get_human_age(
        cat_year: int,
        dog_year: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_year, dog_year) == expected


@pytest.mark.parametrize(
    "cat_year,dog_year,error",
    [
        (-1, 5, ValueError),
        ("five", 9, TypeError),
    ]
)
def test_get_human_age_invalid_types(
        cat_year: int,
        dog_year: int,
        error: type) -> None:
    with pytest.raises(error):
        get_human_age(cat_year, dog_year)
