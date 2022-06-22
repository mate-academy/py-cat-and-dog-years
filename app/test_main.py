from app.main import get_human_age
import pytest


class TestCatDogYears:
    @pytest.mark.parametrize(
        "cat_years, dog_years, human_years",
        [
            pytest.param(
                15, 15,
                [1, 1],
                id="should return 1 human year for first animal years"
            ),
            pytest.param(
                24, 24,
                [2, 2],
                id="should add `extra year` every 9 animal next years"
            ),
            pytest.param(
                28, 29,
                [3, 3],
                id="should add `extra year` every 4 and 5 next years"
            )
        ]
    )
    def test_return_correct_years(self, cat_years, dog_years, human_years):
        assert get_human_age(cat_years, dog_years) == human_years
