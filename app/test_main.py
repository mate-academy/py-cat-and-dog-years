import pytest

from app.main import get_human_age


class TestAnimalsYearsTransfer:
    @pytest.mark.parametrize(
        "cat_years,dog_years,expected_results",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="should return [0, 0] if animals ages are 0's too."
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="should return [0, 0] if animals ages are less then 15"
            ),
            pytest.param(
                17,
                17,
                [1, 1],
                id="should return [1, 1] if animals ages are >= 15 and < 23"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="should return [2, 2] if 24 <= `cat_years` < 28 "
                   "and 24 <= `dog_years` < 29"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="should return [3, 2] if `cat_years` >= 28 "
                   "and 28 <= `dog_years` < 29"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="should return [21, 17] when each animal years are 100"
            ),
            pytest.param(
                -15,
                -24,
                [0, 0],
                id="should return [0, 0] if animals ages are negative numbers"
            )
        ]
    )
    def test_transfer_cat_and_dog_years_to_human(
        self,
        cat_years: int,
        dog_years: int,
        expected_results: list
    ) -> None:
        assert get_human_age(cat_years, dog_years) == expected_results
