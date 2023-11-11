import pytest
from typing import Any


from app.main import get_human_age


class TestAgeForAnimal:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
            (-1, 5, [0, 0]),
            (5, -1, [0, 0]),
            (0, 5, [0, 0]),
            (5, 0, [0, 0]),
            (1000, 2000, [246, 397]),
            (5, 5, [0, 0]),
            (2, 7, [0, 0]),
            (10, 10, [0, 0]),
            (19, 20, [1, 1]),
            (23, 25, [1, 2]),
            (5, 5, [0, 0]),
            (2, 7, [0, 0])
        ]
    )
    def test_get_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected


class TestErrorCases:
    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ("A", 5),
            (10, [5, 6]),
        ]
    )
    def test_error_cases(
            self,
            cat_age: Any,
            dog_age: Any,
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
