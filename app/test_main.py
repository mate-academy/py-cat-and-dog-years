import pytest

from app.main import get_human_age


class Tests:
    @pytest.mark.parametrize(
        "cat_years,dog_years,result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="When dog/cat years = 0, function should be return 0"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="When 0 < dog/cat years < 15, function should be return 0"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="23 cat/dog years should convert into 1 human age."
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="When dog/cat years = 15, func. should be return 1"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="Result should be calculated according to formula"
            )
        ]
    )
    def test_function(self,
                      cat_years: int, dog_years: int, result: list) -> None:
        assert get_human_age(cat_years, dog_years) == result
