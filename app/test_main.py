from typing import Any

import pytest

from app.main import get_human_age


class TestCalculateLimitAges:
    @pytest.mark.parametrize(
        "initial_cat_age, initial_dog_age, expected_result",
        [
            pytest.param(
                0, 0, [0, 0],
                id="When an animals years is zero"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="When an animals less 15 years"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="When an animals 15 years"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="When an animals less 24 years"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="When an animals 24 years"
            ),
            pytest.param(
                27, 27, [2, 2],
                id="When an animals less 28 years"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="When an animals 28 years"
            ),
            pytest.param(
                150, 150, [33, 27],
                id="When an animals 150 years"
            ),
            pytest.param(
                -100, -100, [0, 0],
                id="When an animals -100 years"
            )
        ]
    )
    def test_calculate_human_age(
            self,
            initial_cat_age: int,
            initial_dog_age: int,
            expected_result: list[int]
    ) -> None:
        assert (
            get_human_age(initial_cat_age, initial_dog_age)
        ) == expected_result


class TestsErrorThrowing:
    @pytest.mark.parametrize(
        "initial_cat_age, initial_dog_age, expected_error",
        [
            pytest.param(
                "10", 10, TypeError,
                id="The age of the animals should be by type of integer"
            ),
            pytest.param(
                10, "10", TypeError,
                id="The age of the animals should be by type of integer"
            ),
            pytest.param(
                {10}, "10", TypeError,
                id="The age of the animals should be by type of integer"
            ),
            pytest.param(
                10, {10}, TypeError,
                id="The age of the animals should be by type of integer"
            ),
            pytest.param(
                None, 10, TypeError,
                id="The age of the animals should be by type of integer"
            ),
            pytest.param(
                10, None, TypeError,
                id="The age of the animals should be by type of integer"
            ),
        ]
    )
    def test_should_raise_error_if_arguments_is_not_int(
            self,
            initial_cat_age: Any,
            initial_dog_age: Any,
            expected_error: Any
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(initial_cat_age, initial_dog_age)
