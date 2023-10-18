import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="age_equal_zero"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="age_under_one_year"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="age_exactly_one_year"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="age_under_two_years"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="age_exactly_two_year"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="cat_age_under_three_year"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="dog_age_under_three_year"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="dog_age_under_three_year"
            )
        ]    
    )
    def test_calculates_age_correctly(self, cat_age: int, dog_age: int, expected_result: list):
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_error",
        [
            pytest.param(
                -20,
                -30,
                ValueError,
                id="should raise error whem age < 0"
            ),
            pytest.param(
                999999,
                999999,
                ValueError,
                id="should raise error whem age over expected range"
            ),
            pytest.param(
                "10",
                "10",
                TypeError,
                id="should raise error whem parameters type != int"
            ),
        ]
    )
    def test_expected_errors_raised(self, cat_age, dog_age, expected_error):
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
