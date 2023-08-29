import pytest

from app.main import get_human_age


class Tests:
    @pytest.mark.parametrize(
        "years,result",
        [
            pytest.param(
                14,
                [0, 0],
                id="When dog/cat years < 15, function should be return 0"
            ),
            pytest.param(
                23,
                [1, 1],
                id="23 cat/dog years should convert into 1 human age."
            ),
            pytest.param(
                28,
                [3, 2],
                id="First change should be at 28 years"
            ),
            pytest.param(
                -10,
                [0, 0],
                id="When years are negative function should be return 0"
            ),
            pytest.param(
                100,
                [21, 17],
                id="Result should be calculated according to formula"
            )
        ]
    )
    def test_function(self,
                      years: int, result: list) -> None:
        assert get_human_age(years, years) == result
