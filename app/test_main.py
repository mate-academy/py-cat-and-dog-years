import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_pets_age",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 28, [2, 2]),
            (28, 29, [3, 3]),
            (100, 100, [21, 17]),
        ],
        ids=[
            "both_zero",
            "both_zero_if_years_less_then_15",
            "first_year_both",
            "first_year_both_under_24",
            "second_year_both",
            "second_year_both_under_28_and_29",
            "third_year_both",
            "advanced_age_both"
        ]
    )
    def test_pass(self, cat_age: int, dog_age: int,
                  expected_pets_age: list) -> None:
        assert get_human_age(cat_age, dog_age) == expected_pets_age
