from __future__ import annotations

import pytest

from app.main import get_human_age


class TestHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, human_age",
        [
            pytest.param(
                0, 0, [0, 0],
                id="convert zero ages"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="convert younger 15 years"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="convert 15 years"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="convert 23 years"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="convert 24 years"
            ),
            pytest.param(
                27, 27, [2, 2],
                id="convert between 24-27 years"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="convert cat lower 28"
            ),
            pytest.param(
                28, 29, [3, 3],
                id="convert dog lower 29"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="convert old animals"
            ),
        ]
    )
    def test_should_convert_to_human_years(
            self,
            cat_age: int | float,
            dog_age: int | float,
            human_age: int | float
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_error",
        [
            pytest.param(
                -1, -20, ValueError,
                id="convert negative years"
            ),
            pytest.param(
                "15", 15, TypeError,
                id="convert incorrect type of cat"
            ),
            pytest.param(
                15, "15", TypeError,
                id="convert incorrect type of dog"
            ),
        ]
    )
    def test_raising_errors_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: type[Exception]
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
