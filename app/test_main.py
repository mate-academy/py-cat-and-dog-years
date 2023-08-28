import pytest
from typing import Any
from app.main import get_human_age


class TestGetHumanAge:

    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (23, 23, [1, 1]),
            (38, 24, [5, 2]),
            (100, 100, [21, 17]),
            (-2, -5, [0, 0])
        ],
    )
    def test_human_age_calculated_correctly(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            (
                "zero",
                "zero",
                TypeError,
            ),
            (
                {},
                [],
                TypeError,
            ),
        ]
    )
    def test_raising_error_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Any
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
