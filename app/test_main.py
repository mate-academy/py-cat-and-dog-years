from app.main import get_human_age
import pytest


class TestAnimalToHumanAge:
    @pytest.mark.parametrize(
        "cat_years, dog_years, human_years",
        [
            pytest.param(
                28, 29,
                [3, 3],
                id="28 cat years and 29 dog years should "
                   "convert into 3 human ages",
            ),
            pytest.param(
                24, 24, [2, 2],
                id="24 cat/dog years should convert into 2 human ages",
            ),
            pytest.param(
                15, 15, [1, 1],
                id="15 cat/dog years should convert into 1 human age",
            ),
            pytest.param(
                0, 0, [0, 0],
                id="0 animal years should convert into 0 human ages",
            ),
        ]
    )
    def test_convert_human_ages(self, cat_years, dog_years, human_years):
        assert get_human_age(cat_years, dog_years) == human_years
