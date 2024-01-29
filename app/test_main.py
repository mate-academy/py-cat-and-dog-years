import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, expected, test_id",
    [
        (0, 0, [0, 0], "Test for 0 cat/dog years should return [0, 0]"),
        (14, 14, [0, 0], "Test for 14 cat/dog years should return [0, 0]"),
        (15, 15, [1, 1], "Test for 15 cat/dog years should return [1, 1]"),
        (23, 23, [1, 1], "Test for 23 cat/dog years should return [1, 1]"),
        (24, 24, [2, 2], "Test for 24 cat/dog years should return [2, 2]"),
        (27, 27, [2, 2], "Test for 27 cat/dog years should return [2, 2]"),
        (28, 28, [3, 2], "Test for 28 cat/dog years should return [3, 2]"),
        (100, 100, [21, 17], "Test for 100 years should return [21, 17]"),
        (-1, -1, [0, 0], "Test for negative years should return [0, 0]")

    ]
)
def test_get_human_age(
        cat_years: int,
        dog_years: int,
        expected: str,
        test_id: str
) -> None:
    assert get_human_age(cat_years, dog_years) == expected, test_id
