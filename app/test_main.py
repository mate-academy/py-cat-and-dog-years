import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_years,dog_years, human_years",
        [
            pytest.param(0, 0, [0, 0],
                         id="should_return_zeroes_if_years_are_0"),
            pytest.param(1, 1, [0, 0],
                         id="should_return_zeroes_if_years_are_1"),
            pytest.param(14, 14, [0, 0],
                         id="should_return_zeroes_if_years_less_than_15"),
            pytest.param(15, 15, [1, 1],
                         id="should_return_ones_if_years_are_15"),
            pytest.param(23, 23, [1, 1],
                         id="should_not_add_years_if_less_than_second_limit"),
            pytest.param(24, 24, [2, 2],
                         id="should_correctly_add_years_for_the_second_limit"),
            pytest.param(27, 27, [2, 2],
                         id="should_not_add_years_if_less_than_third_limit"),
            pytest.param(28, 29, [3, 3],
                         id="should_correctly_add_years_for_the_third_limit"),
            pytest.param(100, 100, [21, 17],
                         id="should_correctly_add_years_more_the_third_limit"),
        ]
    )
    def test_returns_correct_years(self,
                                   cat_years: int,
                                   dog_years: int,
                                   human_years: int) -> None:
        assert get_human_age(cat_years, dog_years) == human_years
