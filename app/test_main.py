from app.main import get_human_age
import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_human_age",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="test convert 0 animal years"
            ),
            pytest.param(
                14.9,
                14.9,
                [0, 0],
                id="test convert 14.9 animal years"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="test convert 15 animal years"
            ),
            pytest.param(
                15.1,
                15.1,
                [1, 1],
                id="test convert 15.1 animal years"
            ),
            pytest.param(
                23.9,
                23.9,
                [1, 1],
                id="test convert 23.9 animal years"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="test convert 24 animal years"
            ),
            pytest.param(
                24.1,
                24.1,
                [2, 2],
                id="test convert 24.1 animal years"
            ),
            pytest.param(
                27.9,
                27.9,
                [2, 2],
                id="test convert 27.9 animal years"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="test convert 28 animal years"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="test convert 100 animal years"
            ),

        ]
    )

    def test_convert_animal_years_to_human(
            self,
            cat_age,
            dog_age,
            expected_human_age) -> None:
        assert get_human_age(
            cat_age,
            dog_age
        ) == expected_human_age
