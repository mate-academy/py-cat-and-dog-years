from typing import Any, Type

import pytest

from app.main import get_human_age


class TestCatDogYears:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_ages",
        [
            pytest.param(
                0,
                14,
                [0, 0],
                id=""
                   "test should return human ages equal zero "
                   "when cat or dog ages equal 0 or < 15"
            ),
            pytest.param(
                14,
                15,
                [0, 1],
                id="first 15 cat or dog years should be equal to 1 human year"
            ),
            pytest.param(
                24,
                23,
                [2, 1],
                id="next 9 cat or dog years should give 1 more human year"
            ),
            pytest.param(

                28,
                28,
                [3, 2],
                id="every 4 next cat years should give 1 extra human year"
            ),
            pytest.param(

                28,
                29,
                [3, 3],
                id="every 5 next dog years should give 1 extra human year"
            ),
            pytest.param(

                0,
                0,
                [0, 0],
                id="should return zeros when cat or dog age equals zeros"
            )
        ]
    )
    def test_all_cases(
            self,
            cat_age: int,
            dog_age: int,
            human_ages: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_ages

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                "29", [], AssertionError,
                id="should rise error if age not integer"
            ),
            pytest.param(
                -100, 1000, AssertionError,
                id="should rise error if age not in normal range"
            )
        ]
    )
    def test_correct_errors(
            self,
            cat_age: Any,
            dog_age: Any,
            expected_error: Type[Exception]
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
