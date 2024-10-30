from typing import Type

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
            (100, 100, [21, 17])
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected: list
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
        "cat_age, dog_age, exception",
        [
            ("ten", 10, TypeError),
            (None, 10, TypeError),
            (10, 5.5, TypeError),
            (10, -1, ValueError),
            (-5, -10, ValueError)
        ]
    )
    def test_invalid_inputs(
            self,
            cat_age: any,
            dog_age: any,
            exception: Type[Exception]
    ) -> None:
        """
        Tests that invalid inputs for cat or dog
        age raise the appropriate exceptions.
        """
        with pytest.raises(exception):
            get_human_age(cat_age, dog_age)
