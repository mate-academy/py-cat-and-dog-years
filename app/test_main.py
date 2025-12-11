from typing import Any, List

import pytest

from app.main import get_human_age


class TestAnimalAge:
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
            (-1, 5, [0, 0]),
            (5, -1, [0, 0]),
            (1000, 2000, [246, 397]),
            (10, 10, [0, 0]),
            (19, 20, [1, 1]),
            (23, 25, [1, 2]),
        ]
    )
    def test_get_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected: List[int]
    ) -> None:
        actual = get_human_age(cat_age, dog_age)
        assert actual == expected, (
            f"Expected {expected} when cat's age "
            f"is {cat_age} and dog's age is {dog_age}, "
            f"but got {actual} instead."
        )

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            (5, 5),
            (2, 7),
        ]
    )
    def test_normal_cases(self, cat_age: int, dog_age: int) -> None:
        assert get_human_age(cat_age, dog_age) == [0, 0]

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
        with pytest.raises(TypeError):
            get_human_age(cat_year, dog_year)
