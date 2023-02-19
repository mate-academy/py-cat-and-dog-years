from typing import Any

import pytest

from app.main import get_human_age


class TestConvertAnimalAgeToHuman:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_ages",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
            (-1, -1, [0, 0]),
        ],
    )
    def test_converting_age(
            self,
            cat_age: int,
            dog_age: int,
            expected_ages: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_ages


class TestExpectionsConvertAnimalAgeToHuman:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            ("18", 15, TypeError),
            (18, "15", TypeError),
            ("18", "14", TypeError)
        ],
        ids=[
            "cat_age should be int value",
            "dog_age should be int value",
            "cat_age and dog_age should be int values",
        ],
    )
    def test_raising_error_correctly(
            self,
            cat_age: Any,
            dog_age: Any,
            expected_error: [TypeError]
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
