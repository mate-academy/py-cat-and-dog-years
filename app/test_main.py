from typing import Any, List

import pytest

from app.main import get_human_age


class TestHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
        ]
    )
    def test_typical_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected: List[int]
    ) -> None:
        """
        Tests typical cases for calculating
        human equivalent ages for cats and dogs.
        """
        actual = get_human_age(cat_age, dog_age)
        assert actual == expected, (
            f"Expected {expected} when cat's age "
            f"is {cat_age} and dog's age is {dog_age}, "
            f"but got {actual} instead."
        )

    @pytest.mark.parametrize(
        "cat_year,dog_year",
        [
            (28, 28),
            (100, 100),
            (24, 24),
            (0, 0)
        ]
    )
    def test_range_of_years(
            self,
            cat_year: int,
            dog_year: int
    ) -> None:
        """
        Tests if calculated human ages for cats and dogs
        are within an acceptable range.
        """
        human_cat_year, human_dog_year = get_human_age(cat_year, dog_year)
        assert 0 <= human_cat_year <= 100
        assert 0 <= human_dog_year <= 100

    @pytest.mark.parametrize(
        "cat_year,dog_year",
        [
            ("17", 15),
            ((7 + 5j), (5 + 8j)),
            (None, 15),
            ([24], [24])
        ]
    )
    def test_incorrect_type(
            self,
            cat_year: Any,
            dog_year: Any,
    ) -> None:
        """
        Tests if incorrect data types for cat or dog age
        raise a TypeError.
        """
        with pytest.raises(TypeError):
            get_human_age(cat_year, dog_year)
