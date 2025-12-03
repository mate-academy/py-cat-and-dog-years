from app.main import get_human_age

import pytest


@pytest.mark.parametrize(
    "cat, dog, exp",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21,17])
    ]
)
class TestAnimals:
    def test_if_age_is_integer(self, cat: int, dog: int, exp: list):
        assert all(isinstance(num, int) for num in get_human_age(cat, dog))
    

    def test_if_age_is_positive(self, cat: int, dog: int, exp: list):
        assert all(num >= 0 for num in get_human_age(cat, dog))

    def test_cats_and_dogs_equivalent_age(self, cat: int, dog: int, exp: list):
        assert get_human_age(cat, dog) == exp
