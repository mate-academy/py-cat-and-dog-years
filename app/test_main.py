from app.main import get_human_age
import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "initial_data, expected_result",
        [
            pytest.param(
                [0, 0],
                [0, 0],
                id="should return zeros when animals ages are zeroes"
            ),
            pytest.param(
                [14, 14],
                [0, 0],
                id="should return [0, 0] when animals ages are (14, 14)"
            ),
            pytest.param(
                [15, 15],
                [1, 1],
                id="should return [1, 1] when animals ages are (15, 15)"
            ),
            pytest.param(
                [23, 23],
                [1, 1],
                id="should return [1, 1] when animals ages are (23, 23)"
            ),
            pytest.param(
                [24, 24],
                [2, 2],
                id="should return [2, 2] when animals ages are (24, 24)"
            ),
            pytest.param(
                [27, 27],
                [2, 2],
                id="should return [2, 2] when animals ages are (27, 27)"
            ),
            pytest.param(
                [28, 28],
                [3, 2],
                id="should return [3, 2] when animals ages are (28, 28)"
            ),
            pytest.param(
                [100, 100],
                [21, 17],
                id="should return [21, 17] when animals ages are (100, 100)"
            ),
        ]
    )
    def test_counting_correctly(
            self,
            initial_data: list,
            expected_result: list
    ) -> None:
        assert (
            get_human_age(
                initial_data[0],
                initial_data[1]
            ) == expected_result
        )
