from app.main import get_human_age
import pytest



class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_years, dog_years, expected",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
        ],
        ids=[
            "both_zero",
            "both_14_years",
            "both_15_years",
            "both_23_years",
            "both_24_years",
            "both_27_years",
            "cat_28_years_dog_28_years",
            "both_100_years"
        ]
    )
    def test_correct_behavior(
        self,
        cat_years: int,
        dog_years: int,
        expected: list
    ) -> None:
        assert get_human_age(cat_years, dog_years) == expected
