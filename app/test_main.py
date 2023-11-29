import pytest

from app.main import get_human_age


class TestCalculateLimitValue:
    @pytest.mark.parametrize(
        "initial_cat_age, initial_dog_age, expected_result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="When an animals years is zero"
            ),
            pytest.param(
                14,
                15,
                [0, 1],
            ),
            pytest.param(
                23,
                24,
                [1, 2],
            ),
            pytest.param(
                24,
                30,
                [2, 3],
                id="When an animals years greeter than a human"
            ),
            pytest.param(
                27,
                28,
                [2, 2],
                id="Discard the remainder result"
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="Discard the remainder result"
            )
        ]
    )
    def test_calculate_limit_value(
            self,
            initial_cat_age: int,
            initial_dog_age: int,
            expected_result: list
    ) -> None:
        assert (
            get_human_age(initial_cat_age, initial_dog_age)
        ) == expected_result
