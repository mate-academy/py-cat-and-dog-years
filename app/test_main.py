import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "initial_ages, expected_result",
        [
            pytest.param(
                (-13, 18),
                [0, 1],
                id="one of ages is negative"
            ),
            pytest.param(
                (0, 19.38),
                [0, 1],
                id="if age is 0 or float"
            ),
            pytest.param(
                (14, 14),
                [0, 0],
                id="less then 15 age"
            ),
            pytest.param(
                (15, 23),
                [1, 1],
                id="age is from 15 to 23"
            ),
            pytest.param(
                (80, 24),
                [16, 2],
                id="age is more than 24"
            ),
            pytest.param(
                (28, 28),
                [3, 2],
                id="different amount of human years after 24"
            )
        ]
    )
    def test_for_correct_results(
            self,
            initial_ages: tuple,
            expected_result: list
    ) -> None:
        assert get_human_age(*initial_ages) == expected_result

    @pytest.mark.parametrize(
        "test_value, expected_error",
        [
            pytest.param(
                ("age", [], (), dict),
                TypeError,
                id="error when not a number was entered"
            ),
        ],
    )
    def test_for_incorrect_age(
            self,
            test_value: tuple,
            expected_error: Exception
    ) -> None:
        for value in test_value:
            with pytest.raises(expected_error):
                get_human_age(value, 15)
                get_human_age(15, value)
