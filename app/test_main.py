import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="Test should 0 zeros if ages equal 0"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="Test should return 0 if ages less than first year"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="Test should return 1 if ages equal first year"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="Test should return 1 if ages between first and second year"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="Test should return 2 if ages between equal second year"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="Test should return 2 if ages over second year"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="Test should return 21 and 17 if ages equal 100 year"
            ),
        ]
    )
    def test_get_human_age_correct(self,
                                   cat_age: int,
                                   dog_age: int,
                                   result: list) -> None:
        assert get_human_age(cat_age, dog_age) == result
