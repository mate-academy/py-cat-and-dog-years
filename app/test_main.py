from app.main import get_human_age
import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_years,dog_years,excepted_years",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="Test years when cat and dogs years"
                   " equal 0"),

            pytest.param(
                14,
                14,
                [0, 0],
                id="Test correct counting cat and dog years"
                   " if years < 15"),

            pytest.param(
                15,
                15,
                [1, 1],
                id="Test first 15 dog and cat years"
                   " give 1 human year"),

            pytest.param(
                27,
                27,
                [2, 2],
                id="Finally test when cat and dogs years"
                   " must be equal"),

            pytest.param(
                28,
                28,
                [3, 2],
                id="Test when cat years must be more"
                   " then dogs years in range 28 year."),

            pytest.param(
                100,
                100,
                [21, 17],
                id="Finally test in range, when the cat"
                   " years go forward overtaking dogs years")])
    def test_human_age_correctly(self,
                                 cat_years: int,
                                 dog_years: int,
                                 excepted_years: list):
        assert get_human_age(cat_years, dog_years) == excepted_years
