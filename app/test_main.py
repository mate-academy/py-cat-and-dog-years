import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "initial_cat_years,initial_dog_years,expected_human_years",
        [
            pytest.param(0, 0, [0, 0]),
            pytest.param(14, 14, [0, 0]),
            pytest.param(15, 15, [1, 1]),
            pytest.param(23, 23, [1, 1]),
            pytest.param(24, 24, [2, 2]),
            pytest.param(27, 27, [2, 2]),
            pytest.param(28, 29, [3, 3]),
            pytest.param(28, 28, [3, 2]),
            pytest.param(27, 29, [2, 3]),
            pytest.param(100, 100, [21, 17]),
            pytest.param(0, 100, [0, 17]),
            pytest.param(100, 0, [21, 0]),
            pytest.param(1000, 5000, [246, 997]),
        ],
        ids=[
            "get_human_age_when_both_ages_are_zero",
            "get_human_age_when_both_ages_are_below_first_threshold",
            "get_human_age_when_both_ages_are_equal_to_first_threshold",
            "get_human_age_when_both_ages_are_between_1st_and_2nd_threshold",
            "get_human_age_when_both_ages_are_equal_to_second_threshold",
            "get_human_age_when_both_ages_not_reaches_next_level",
            "get_human_age_when_both_reach_next_level",
            "get_human_age_when_cat_reaches_next_level_but_dog_does_not",
            "get_human_age_when_dog_reaches_next_level_but_cat_does_not",
            "get_human_age_for_large_ages",
            "get_human_age_when_only_cat_age_is_zero",
            "get_human_age_when_only_dog_age_is_zero",
            "get_human_age_for_extra_large_ages"
        ],
    )
    def test_convert_cat_and_dog_age_into_human_age_correctly(
        self,
        initial_cat_years: int,
        initial_dog_years: int,
        expected_human_years: list[int],
    ) -> None:
        assert (
            get_human_age(initial_cat_years, initial_dog_years)
            == expected_human_years
        )

    @pytest.mark.parametrize(
        "initial_cat_years,initial_dog_years,expected_error",
        [
            pytest.param(-1, 15, ValueError),
            pytest.param(15, -1, ValueError),
            pytest.param("1", 15, TypeError),
            pytest.param(15, "1", TypeError),
        ],
        ids=[
            "should_raise_error_if_cat_age_less_than_zero",
            "should_raise_error_if_dog_age_less_than_zero",
            "should_raise_error_if_cat_age_not_int",
            "should_raise_error_if_dog_age_not_int",
        ],
    )
    def test_raising_errors_correctly(
        self,
        initial_cat_years: int,
        initial_dog_years: int,
        expected_error: type[ValueError | TypeError],
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(initial_cat_years, initial_dog_years)
