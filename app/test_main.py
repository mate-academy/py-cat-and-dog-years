from app.main import get_human_age
import pytest


@pytest.mark.parametrize("cat_year, dog_year, result", [
    (0, 0, [0, 0]),
    (14, 0, [0, 0]),
    (15, 0, [1, 0]),
    (24, 0, [2, 0]),
    (28, 0, [3, 0]),
    (0, 14, [0, 0]),
    (0, 15, [0, 1]),
    (0, 24, [0, 2]),
    (0, 29, [0, 3]),
    (20, 30, [1, 3]),
    (0, 23, [0, 1]),
])
def test_can_sum(cat_year: int, dog_year: int, result: list) -> None:
    assert get_human_age(cat_year, dog_year) == result
