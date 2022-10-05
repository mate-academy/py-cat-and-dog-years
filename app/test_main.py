import pytest

from app.main import get_human_age


class TestCatAndDogYears:
    @pytest.mark.parametrize(
        "cat_years, dog_years, expended_years",
        [

            pytest.param(
                0, 0, [0, 0],
                id="Should return [0, 0] when years equals zero"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="Should return [0, 0] when years <= 15 years"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="Should return [1, 1] when age cat equals\
                 15 and dog age equals 15"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="Should return [2, 2] when age cat equals\
                 24 and dog age equals 24"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="Should return [3, 2] when age cat and dog equals 28"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="Should return [21, 17] when age cat and dog equals 100"
            )
        ]
    )
    def test_get_human_age(self, cat_years, dog_years, expended_years):
        assert get_human_age(cat_years, dog_years) == expended_years
