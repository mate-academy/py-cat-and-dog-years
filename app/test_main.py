from app.main import get_human_age
from typing import List
import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize("initial_value, value, expected", [
        pytest.param(
            0,
            0,
            [0, 0],
            id="On receipt, 0 should return the same age"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="First human year has 15 years of cats or dogs live"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="15 years should be equal to one human year"
        ),

        pytest.param(
            24,
            24,
            [2, 2],
            id="24 years should be converted into 2 human years"
        ),

        pytest.param(
            28,
            28,
            [3, 2],
            id="Cats years shouldn't be counted the same as dogs"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="Should be correctly calculated according to the requirements"
        ),
    ])
    def test_main(
            self,
            initial_value: int,
            value: int,
            expected: List[int]
    ) -> None:
        assert get_human_age(initial_value, value) == expected
