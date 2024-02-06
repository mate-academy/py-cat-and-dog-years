import pytest
from typing import Any

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
        [
            (1, 1, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (24, 24, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
        ],
        ids=[
            "less 15 cat and dog years give 0 human year",
            "less 15 cat and dog years give 0 human year",
            "first 15 cat and dog years give 1 human year",
            "from 15 to 23 cat and dog years give 1 more human year",
            "after 23 years every 4 next cat years give 1 extra human year",
            "after 23 years every 5 next dog years give 1 extra human year",
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected: list[int]
    ) -> None:
        result = get_human_age(cat_age, dog_age)
        assert result == expected

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            ("1", 1, TypeError),
            (2, "2", TypeError),
            ("2", "2", TypeError),
        ],
        ids=[
            "cat age must be an integer",
            "dog age must be an integer",
            "cat and dog age must be integer"
        ]
    )
    def test_get_human_age_error(self, cat_age: Any, dog_age: Any,
                                 expected_error: TypeError) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
