from app.main import get_human_age
import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, human_age",
        [
            pytest.param(
                0, 0, [0, 0],
                id="should convert min value"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="should convert max for zero years"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="should convert min for one year"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="should convert max for one year"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="should convert min for two years"
            ),
            pytest.param(
                27, 28, [2, 2],
                id="should convert max for two years"
            ),
            pytest.param(
                28, 29, [3, 3],
                id="should convert min for three years"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="should convert max value"
            )
        ]
    )
    def test_get_human_age(
            self,
            cat_age,
            dog_age,
            human_age
    ):
        result = get_human_age(cat_age, dog_age)
        assert result == human_age
