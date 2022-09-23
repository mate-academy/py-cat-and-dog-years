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
                id="0, 0 -> should return 0"
                   " when cat and dog 0"),

            pytest.param(
                14,
                14,
                [0, 0],
                id="14, 14 -> should return 0"
                   " when cat and dog years less than 15"),

            pytest.param(
                15,
                15,
                [1, 1],
                id="15, 15 -> should return 1"
                   " when cat and dog years equal 15"),

            pytest.param(
                27,
                27,
                [2, 2],
                id="27, 27 -> should return 2,"
                   " when cat and dog years 27"),

            pytest.param(
                28,
                28,
                [3, 2],
                id=" should return 3 for cat and 2"
                   " for dog when years equal to 28."),

            pytest.param(
                100,
                100,
                [21, 17],
                id="100, 100 -> should work correct with big numbers")])
    def test_human_age_correctly(self,
                                 cat_years: int,
                                 dog_years: int,
                                 excepted_years: list):
        assert get_human_age(cat_years, dog_years) == excepted_years
