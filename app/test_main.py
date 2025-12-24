import pytest

from app.main import get_human_age


class TestGetHumanAge:

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_age_list",
        [
            pytest.param(
                0, 17,
                [0, 1],
                id="should return 0 when age is 0"
            ),
            pytest.param(
                15, 14,
                [1, 0],
                id="should return 0 when age is less than first border"
            ),
            pytest.param(
                23, 24,
                [1, 2],
                id="should return 1 when age between first and second border"
            ),
            pytest.param(
                28, 28,
                [3, 2],
                id="should return 2 when age between second and third border"
            ),
            pytest.param(
                38, 34,
                [5, 4],
                id="should return correct age when input is above third border"
            )
        ]
    )
    def test_returns_correct_age(self, cat_age, dog_age, expected_age_list):
        age = get_human_age(cat_age, dog_age)
        assert age == expected_age_list
