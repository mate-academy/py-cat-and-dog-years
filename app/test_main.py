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
            (72, 29, [14, 3]),
            (34, 11, [4, 0]),
            (100, 100, [21, 17]),
            (-1, -1, [0, 0]),
        ],
        ids=[
            "cat 0, dog 0",
            "cat 14, dog 14",
            "cat 15, dog 15",
            "cat 23, dog 23",
            "cat 24, dog 24",
            "cat 27, dog 27",
            "cat 28, dog 28",
            "cat 72, dog 29",
            "cat 34, dog 11",
            "cat 100, dog 100",
            "cat -1, dog -1",
        ],
    )
    def test_converting_age(
            self,
            cat_age: int,
            dog_age: int,
            expected_ages: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_ages

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
