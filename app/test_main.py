import pytest

from app.main import get_human_age


class TestGetAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_age_values",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="must return 0 for both animals"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="must return 0 for both animals"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="must add 1 year in both cases"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="must add only 1 year in both cases"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="must add 2 years in both cases"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="must be 3 years for cat age and 2 years for dog age"
            ),
            pytest.param(
                65,
                65,
                [12, 10],
                id="must return the correct age for every next years"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="must return the correct age for every next years"
            ),
            pytest.param(
                123456789,
                123456789,
                [30864193, 24691355],
                id="must return the correct age with large numbers"
            ),
            pytest.param(
                -10,
                -10,
                [0, 0],
                id="must return zero when negative value of years"
            ),
            pytest.param(
                100.0,
                100.0,
                [21.0, 17.0],
                id="must return correct float values"
            )
        ]
    )
    def test_get_correct_human_age(self,
                                   cat_age: int,
                                   dog_age: int,
                                   expected_age_values: list) -> None:
        assert get_human_age(cat_age, dog_age) == expected_age_values

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                "16",
                16,
                TypeError,
                id="must return 'TypeError' if not int"
            ),
            pytest.param(
                25,
                "25",
                TypeError,
                id="must return 'TypeError' if not int"
            )
        ]
    )
    def test_invalid_input(self,
                           cat_age: int,
                           dog_age: int,
                           expected_error: Exception) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
