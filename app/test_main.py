from typing import Any

import pytest
from app.main import get_human_age


class TestCatDog:

    @pytest.mark.parametrize(
        "cat_years_old, dog_years_old, human_age",
        [
            pytest.param(
                14,
                14,
                [0, 0],
                id="should return 0 human year"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="should return 1 human year"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="should return 2 human year"
            ),
            pytest.param(
                27,
                28,
                [2, 2],
                id="should return 2 human year"
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="should return 3 human year"
            ),
            pytest.param(
                0,
                0,
                [0, 0],
                id="should return 0 human year"
            )
        ]
    )
    def test_convert_correctly(
            self,
            cat_years_old: int,
            dog_years_old: int,
            human_age: int
    ) -> None:
        assert get_human_age(cat_years_old, dog_years_old) == human_age

    @pytest.mark.parametrize(
        "cat_years_old, dog_years_old, expected_error",
        [
            pytest.param(
                "string",
                "text",
                TypeError,
                id="should raise error when parameter is not int"
            ),
        ]
    )
    def test_raising_errors_correctly(self,
                                      cat_years_old: int,
                                      dog_years_old: int,
                                      expected_error: Any
                                      ) -> None:
        with pytest.raises(expected_error):
            assert get_human_age(cat_years_old, dog_years_old)
