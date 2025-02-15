import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (25, 25, [2, 2]),
        (29, 29, [3, 3]),
        (35, 35, [4, 4]),
    ]
)
def test_get_human_age(cat_years: int, dog_years: int, expected: int) -> None:
    assert get_human_age(cat_years, dog_years) == expected
