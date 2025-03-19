from app.main import get_human_age
import pytest


#  list for testing
@pytest.mark.parametrize(
    "cat_years, dog_years, expected",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (0, 0, [0, 0]),
        (-10, -25, [0, 0]),
        (110, 125, [23, 22])

    ]
)
def test_value(cat_years: int, dog_years: int, expected: int) -> None:
    assert get_human_age(cat_years, dog_years) == expected
