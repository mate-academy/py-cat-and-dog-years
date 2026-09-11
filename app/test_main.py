import pytest

from typing import Any

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "initial_cat_age,initial_dog_age,expected_result",
        [
            (
                0, 0, [0, 0]
            ),
            (
                14, 14, [0, 0]
            ),
            (
                15, 15, [1, 1]
            ),
            (
                24, 24, [2, 2]
            ),
            (
                28, 28, [3, 2]
            ),
            (
                15, 14, [1, 0]
            ),
            (
                100, 100, [21, 17]
            ),
            (
                -1, -5, [0, 0]
            ),
            (
                1000, 1500, [246, 297]
            )
        ]
    )
    def test_convert_to_human_age(self: object,
                                  initial_cat_age: int,
                                  initial_dog_age: int,
                                  expected_result: list) -> None:
        assert get_human_age(initial_cat_age,
                             initial_dog_age) == expected_result

    @pytest.mark.parametrize(
        "initial_cat_age,initial_dog_age,expected_error",
        [
            pytest.param(
                [7], 8, TypeError,
                id="error if type not integer"
            )
        ]
    )
    def test_raising_errors_corectly(self: object,
                                     initial_cat_age: Any,
                                     initial_dog_age: Any,
                                     expected_error: Any) -> None:
        with pytest.raises(expected_error):
            get_human_age(initial_cat_age, initial_dog_age)
