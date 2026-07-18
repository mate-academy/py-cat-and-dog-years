from __future__ import annotations

import pytest

from app.main import get_human_age


class TestCat:
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
                id="convert lower limit from 15 to 23 years old"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="convert higher limit from 15 to 23 years old"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="convert lower limit over 24 years old"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="convert over 24 years of different ages"
            )
        ]
    )
    def test_should_convert_to_human_years(
            self,
            cat_age: int | float,
            dog_age: int | float,
            human_age: int | float
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age
