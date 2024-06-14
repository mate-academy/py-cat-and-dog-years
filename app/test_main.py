import pytest
from typing import Type

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_years, dog_years, converted_human_years",
        [
            pytest.param(
                0, 0, [0, 0],
                id="test should return list of zeros if input values are zeros"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="should return zeros if animal ages are < 15"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="should return ones if animal ages = 15"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="should calculate cats and dogs age differently"
            ),
            pytest.param(
                -10, 24, [0, 2],
                id="should handle negative numbers"
            ),
            pytest.param(
                10000, 10000, [2496, 1997],
                id="should handle very large numbers"
            )
        ]
    )
    def test_calculate_human_age_correctly(
            self,
            cat_years: int,
            dog_years: int,
            converted_human_years: [int, int]
    ) -> None:
        result = get_human_age(cat_years, dog_years)
        assert result == converted_human_years

    @pytest.mark.parametrize(
        "cat_years, dog_years, expected_error",
        [
            pytest.param(
                28, "two", TypeError,
                id="should return TypeError "
                   "if one of the values is not integer"
            ),
        ]
    )
    def test_raising_errors_correctly(
            self,
            cat_years: int,
            dog_years: int,
            expected_error: Type[BaseException]
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_years, dog_years)
