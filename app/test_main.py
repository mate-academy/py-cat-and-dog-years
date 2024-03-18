from typing import Any

import pytest

from app.main import get_human_age


class TestGetHumanAge:

    @pytest.mark.parametrize(
        "age,expected",
        [
            (-1, [0, 0]),
            (0, [0, 0]),
            (14, [0, 0]),
            (15, [1, 1]),
            (23, [1, 1]),
            (24, [2, 2]),
            (27, [2, 2]),
            (28, [3, 2]),
            (100, [21, 17]),
            (10000, [2496, 1997]),
        ],
        ids=[
            "Negative years animal should into 0 human age",
            "Before 15 years animal should into 0 human age",
            "Before 15 years animal should into 0 human age",
            "First 15 years animal should into 1 human age",
            "First 15 years animal should into 1 human age",
            "The next 9 years after first 15 year animal "
            "give 1 more human age",
            "The next 9 years after first 15 year animal "
            "give 1 more human age",
            "Every 4 cat and 5 dog years after 24 years animal "
            "give 1 extra human year",
            "Every 4 cat and 5 dog years after 24 years animal "
            "give 1 extra human year",
            "Every 4 cat and 5 dog years after 24 years animal "
            "give 1 extra human year"
        ]
    )
    def test_correct_get_human_age(
            self,
            age: int,
            expected: list[int]
    ) -> None:
        assert get_human_age(age, age) == expected

    @pytest.mark.parametrize(
        "wrong_type_age",
        [
            "age",
            [0, 0],
            None,
            {0, 0},
            {0: 0}
        ]
    )
    def test_incorrect_type_get_human_age(self, wrong_type_age: Any) -> None:
        with pytest.raises(TypeError):
            get_human_age(wrong_type_age, wrong_type_age)
