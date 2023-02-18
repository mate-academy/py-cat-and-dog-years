import pytest

from app.main import get_human_age


class TestHumanCatDogYears:
    @pytest.mark.parametrize(
        "cat_years,dog_years,human_years",
        [
            (14, 14.22, [0, 0]),
            (1, 1, [0, 0]),
            (0, 0, [0, 0]),
            (-3, -12, [0, 0]),
            (15, 15, [1, 1]),
            (23.9, 23.9, [1, 1]),
            (24.0, 24.96, [2, 2]),
            (27.96, 28.0, [2, 2]),
            (28.0, 29.0, [3, 3]),
            (10000, 10000, [2496, 1997]),
        ],
        ids=[
            "`human_years` should equal `catdog_till_15` max",
            "`human_years` should equal `catdog_till_15` min",
            "should correctly work with zeros",
            "should correctly work with negative numbers",
            "`human_years` should equal `catdog_15_24` min",
            "`human_years` should equal `catdog_15_24` max",
            "`human_years` should equal `catdog_24` min",
            "`human_years` should equal `catdog_24` max",
            "`human_years` should equal `catdog_24+` min",
            "`human_years` should equal `catdog_24+` big_num"
        ]
    )
    def test_results_should_equal_correct_period(
            self,
            cat_years: int | float,
            dog_years: int | float,
            human_years: int | float
    ) -> None:
        assert get_human_age(cat_years, dog_years) == human_years


class TestErrorTypes:
    def test_type_error_missing_1_positional_argument(self) -> None:
        with pytest.raises(TypeError, match=r".* missing 1 *."):
            get_human_age(1)

    def test_type_error_expected_2_ints(self) -> None:
        with pytest.raises(TypeError):
            get_human_age(1, False)
