import pytest

from typing import Any

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "age,expected_age",
        [
            (-1, [0, 0]),
            (0, [0, 0]),
            (14, [0, 0]),
            (15, [1, 1]),
            (23, [1, 1]),
            (24, [2, 2]),
            (27, [2, 2]),
            (28, [3, 2]),
            (100, [21, 17])
        ],

        ids=[
            "Negative years should converted to 0 human age",
            "Age under 15 should be equal to 0 human age",
            "Age under 15 should be equal to 0 human age",
            "The first 15 years must be converted into 1 human year",
            "The first 15 years must be converted into 1 human year",

            "The first 15 years must be converted into 1 human year "
            "and the next 9 cat and dog years give 1 more human year",

            "The first 15 years must be converted into 1 human year "
            "and the next 9 cat and dog years give 1 more human year",

            "Every 4 next cat years after 24 give 1 extra human year "
            "and every 5 next dog years give 1 extra human year",

            "Every 4 next cat years after 24 give 1 extra human year "
            "and every 5 next dog years give 1 extra human year"
        ]
    )
    def test_get_human_age(self, age: int, expected_age: list[int]) -> None:
        assert get_human_age(age, age) == expected_age

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
    def test_wrong_type_get_human_age(self, wrong_type_age: Any) -> None:
        with pytest.raises(TypeError):
            get_human_age(wrong_type_age, wrong_type_age)
