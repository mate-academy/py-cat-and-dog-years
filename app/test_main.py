from typing import Any
import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age, expected_result",
        [
            pytest.param(
                -44,
                -3,
                [0, 0],
                id="should return 0 for both cat and dog ages under zero",
            ),
            pytest.param(
                14, 14, [0, 0], id="check age under 1 for both cat and dog"
            ),
            pytest.param(
                15, 15, [1, 1], id="check age equals 1 for both cat and dog"
            ),
            pytest.param(
                23, 23, [1, 1], id="check age equals 1 for both cat and dog"
            ),
            pytest.param(
                24, 24, [2, 2], id="check age equals 2 for both cat and dog"
            ),
            pytest.param(
                27, 28, [2, 2], id="check age equals 2 for both cat and dog"
            ),
            pytest.param(
                28, 29, [3, 3], id="check age equals 3 for both cat and dog"
            ),
            pytest.param(
                314,
                314,
                [74, 60],
                id="check high age conversion for both cat and dog",
            ),
        ],
    )
    def test_should_return_correctly_converted_age(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            ([0], [4], TypeError),
            ("15", "23", TypeError),
            ({15}, {23}, TypeError),
        ]
    )
    def test_correct_error(self, cat_age: Any, dog_age: Any, expected_error: Exception):
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
