import pytest
from typing import Any
from app.main import get_human_age


class TestGradationOfYears:

    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="zero year"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="before first year"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="first year"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="before second year"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="second year"
            ),
            pytest.param(
                27,
                28,
                [2, 2],
                id="before each_year"
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="each_year"
            ),
            pytest.param(
                -20,
                -30,
                [0, 0],
                id="negative age of animals"
            ),
            pytest.param(
                40,
                44,
                [6, 6],
                id="unattainable age for animals"
            )
        ]
    )
    def test_gradation_of_years(
        self,
        cat_age: int,
        dog_age: int,
        result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result

    @pytest.mark.parametrize(
        "cat_age,dog_age",
        [
            pytest.param(
                "15",
                "15",
                id="type streng"
            ),
            pytest.param(
                [],
                [],
                id="type list"
            ),
            pytest.param(
                {},
                {},
                id="type dict"
            )
        ]
    )
    def test_of_error(
        self,
        cat_age: Any,
        dog_age: Any
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
