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
        (100, 100, [21,17])
    ]
)
class TestAnimals:
    def test_if_age_is_integer(self, cat: int, dog: int, exp: list):
        assert type(cat) == int
        assert type(dog) == int
        assert all(isinstance(num, int) for num in get_human_age(cat, dog))

    def test_cats_and_dogs_equivalent_age(self, cat: int, dog: int, exp: list):
        expected = exp
        actual = get_human_age(cat, dog)
        assert expected == actual
