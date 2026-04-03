import pytest
from app.main import get_human_age

class TestHumanAgeClass:
    @pytest.mark.parametrize(
        "initial_age_cat, initial_age_dog, expected_ages",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="should return list"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="should return_zero years"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="should return one year"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="should return another stage of animals year"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="should return second stage of animals year"
            ),
            pytest.param(
                27,
                28,
                [2, 2],
                id="should return another1 stage of animals year"
            ),
            pytest.param(
                28,
                30,
                [3, 3],
                id="should return third stage of animals year"
            )
        ]
    )
    def test_get_human_age(self, initial_age_cat, initial_age_dog, expected_ages) -> None:
        assert get_human_age(initial_age_cat, initial_age_dog) == expected_ages

