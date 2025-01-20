import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, expected",
    [
        (0, 0, [0, 0]),
        (20, 20, [2, 2]),
        (200, 200, [46, 37]),
        (-200, -200, [0, 0]),
        (14, 23, [0, 1])
    ]
)
def test_get_human_age(cat_years: int, dog_years: int, expected: int) -> None:
    assert get_human_age(cat_years, dog_years) == expected
