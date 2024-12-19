from app.main import get_human_age
import pytest


@pytest.mark.parametrize("cat_years, dog_years, expected", [
    (0, 0, [0, 0]),
    (13, 13, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (20, 20, [1, 1]),
    (23, 23, [1, 1]),
    (27, 26, [1, 1]),
    (28, 28, [3, 2]),
    (30, 30, [3, 2]),
    (100, 100, [21, 17]),
])
def test_cat_and_dog_to_human_age(cat_years: int,
                                  dog_years: int,
                                  expected: list) -> None:
    assert get_human_age(cat_years, dog_years) == expected
