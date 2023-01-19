import pytest
from app.main import get_human_age


class TestAge:
    @pytest.mark.parametrize(
        "initial_1, initial_2, result",
        [
            pytest.param(
                28, 28,
                [3, 2],
                id="test check that it is not changed with previous value"
            ),
            pytest.param(
                -1, 0,
                [0, 0],
                id="test receives data out of normal range"
            ),
            pytest.param(
                1000, 0,
                [246, 0],
                id="test receives data of large numbers"
            ),
            pytest.param(
                25.5, 45.1,
                [2, 6],
                id="test receives an float type of data"
            )
        ]
    )
    def test_get_human_age(self, initial_1, initial_2, result):
        assert get_human_age(initial_1, initial_2) == result

    @pytest.mark.parametrize(
        "initial_1, initial_2, expected_error",
        [
            pytest.param(
                "15", 1, TypeError,
                id="test receives an str type of data"
            ),
            pytest.param(
                [], 1, TypeError,
                id="test receives an list type of data"
            ),
            pytest.param(
                {}, 1, TypeError,
                id="test receives an dict type of data"
            ),
            pytest.param(
                (), 1, TypeError,
                id="test receives an set type of data"
            )
        ]
    )
    def test_get_human_age_errors(self, initial_1, initial_2, expected_error):
        with pytest.raises(expected_error):
            get_human_age(initial_1, initial_2)
