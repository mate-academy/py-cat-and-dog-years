import pytest

from app.main import get_human_age


class TestParseFirstYears:
    @pytest.mark.parametrize(
        "animal_years, result",
        [
            pytest.param(
                [0, 0],
                [0, 0],
                id="test_zero_years"

            ),
            pytest.param(
                [14, 14],
                [0, 0],
                id="last_year_before_first_human_year"

            ),
            pytest.param(
                [15, 15],
                [1, 1],
                id="test_first_human_year_starts_at_15"
            ),
            pytest.param(
                [23, 23],
                [1, 1],
                id="test_last_year_before_second_human_year"

            ),
            pytest.param(
                [24, 24],
                [2, 2],
                id="test_second_human_year_starts_at_24"
            ),
            pytest.param(
                [27, 27],
                [2, 2],
                id="test_last_year_before_cat_third_human_year"
            ),
            pytest.param(
                [28, 28],
                [3, 2],
                id="test_cat_gets_third_year_dog_does_not"
            ),
            pytest.param(
                [100, 100],
                [21, 17],
                id="test_big_numbers_calculation"
            ),
        ]
    )
    def test_first_years(
            self,
            animal_years: list[int],
            result: list[int]) -> None:
        assert get_human_age(animal_years[0], animal_years[1]) == result
