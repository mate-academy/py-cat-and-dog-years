import pytest
from typing import Type

from app.main import get_human_age


class TestAnimalAges:

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
    def test_basically_ages_human_is_equal_to_animal(
            self,
            cat_age: int,
            dog_age: int,
            expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (-3, 0, [0, 0]),
            (0, -4, [0, 0]),
            (-5, -6, [0, 0]),
        ]
    )
    def test_negative_value(
            self,
            cat_age: int,
            dog_age: int,
            expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected


class TestErrorCase:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_error",
        [
            (0, bool, TypeError),
            (3.5, "cat", TypeError),
        ]
    )
    def test_error_type_ages(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Type[Exception]
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
