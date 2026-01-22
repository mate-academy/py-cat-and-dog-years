import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat, dog, expected",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
class TestAnimal:

    def test_cat_and_dog_less_than_fifteen_years(self, cat: int,
                                                 dog: int,
                                                 expected: list) -> None:
        assert get_human_age(cat, dog) == expected

    def test_cat_and_dog_with_fifteen_years(self, cat: int,
                                            dog: int, expected: list) -> None:
        assert get_human_age(cat, dog) == expected

    def test_all_animals_with_23_years(self, cat: int,
                                       dog: int, expected: list) -> None:
        assert get_human_age(cat, dog) == expected

    def test_all_animals_with_24_years(self, cat: int,
                                       dog: int, expected: list) -> None:
        assert get_human_age(cat, dog) == expected

    def test_all_animals_with_27_years(self, cat: int,
                                       dog: int, expected: list) -> None:
        assert get_human_age(cat, dog) == expected

    def test_all_animals_with_28_years(self, cat: int,
                                       dog: int, expected: list) -> None:
        assert get_human_age(cat, dog) == expected

    def test_all_animals_with_100_years(self, cat: int,
                                        dog: int, expected: list) -> None:
        assert get_human_age(cat, dog) == expected
