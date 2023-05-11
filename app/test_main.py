import pytest
from typing import Any
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(
                -1,
                -3,
                [0, 0],
                id="should return zero if negative age",
            ),

            pytest.param(
                0,
                0,
                [0, 0],
                id="should return zero if age is zero",
            ),

            pytest.param(
                14,
                14,
                [0, 0],
                id="should return zero if less than one human year",
            ),

            pytest.param(
                15,
                15,
                [1, 1],
                id="should return 1 year if animal years are 15",
            ),

            pytest.param(
                28,
                28,
                [3, 2],
                id="should return correct year if human years are different",
            ),
        ]
    )
    def test_return_correct_age(
            self, cat_age: int, dog_age: int, expected_result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age, dog_age, error",
        [
            pytest.param([], [], TypeError, id="Wrong type"),
        ]
    )
    def test_raise_typeerror(
            self, cat_age: Any, dog_age: Any, error: type[TypeError]
    ) -> None:
        with pytest.raises(error):
            get_human_age(cat_age, dog_age)
