import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "values, expected_result",
        [
            (
                (0, 0),
                [0, 0]
            ),
            (
                (15, 15),
                [1, 1]
            ),
            (
                (24, 24),
                [2, 2]
            ),
            (
                (28, 28),
                [3, 2]
            ),
            (
                (100, 100),
                [21, 17]
            )
        ]
    )
    def test_should_return_correct_values(
        self,
        values,
        expected_result
    ):
        res = get_human_age(*values)
        assert res == expected_result
