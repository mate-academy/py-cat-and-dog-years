import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, result",
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
        "both years are 0",
        "both years are under 15",
        "both years are 15",
        "not enough for 2 human years",
        "exactly 2 years each",
        "not enough for 3 human years",
        "equal cat and dog years, not equal human",
        "equal big cat and dog years, not equal human",
    ]
)
def test_can_calculate_age_properly(
        cat_years: int,
        dog_years: int,
        result: int
) -> None:
    assert get_human_age(cat_years, dog_years) == result
