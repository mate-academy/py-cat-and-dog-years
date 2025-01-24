import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years,dog_years,expected",
    [
        (-10, -10, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (14, 15, [0, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (5243, 8018, [1306, 1600])
    ]
)
def test_get_human_age(cat_years: int, dog_years: int, expected: list) -> None:
    assert (get_human_age(cat_years, dog_years)) == expected
