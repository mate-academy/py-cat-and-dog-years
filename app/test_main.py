import pytest


from app.main import get_human_age


class TestHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(
                0, 0, [0, 0],
                id="should_return_zeros_when_ages_are_equal_to_zero"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="should_return_zeros_when_ages_are_less_than_15"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="should_return_ones_when_ages_are_equal_first_year"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="should_return_ones_when_ages_are_between_first_and_second_years"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="should_return_two_when_ages_are_equal_second_year"
            ),
            pytest.param(
                27, 28, [2, 2],
                id="should_return_two_when_ages_are_below_third_year"
            ),
            pytest.param(
                28, 29, [3, 3],
                id="should_return_three_when_ages_are_equal_third_year"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="should_return_correct_value_when_ages_are_bigger_than_third_year"
            ),
        ]
    )
    def test_count_human_age(
            self,
            cat_age,
            dog_age,
            expected_result
    ):
        assert get_human_age(cat_age, dog_age) == expected_result


# def test_should_return_zeros_when_ages_are_less_than_15():
#     assert get_human_age(14, 14) == [0, 0]
#
#
# def test_should_return_zeros_when_ages_are_equal_to_zero():
#     assert get_human_age(0, 0) == [0, 0]
#
#
# def test_should_return_ones_when_ages_are_equal_first_year():
#     assert get_human_age(15, 15) == [1, 1]
#
#
# def test_should_return_ones_when_ages_are_between_first_and_second_years():
#     assert get_human_age(23, 23) == [1, 1]
#
#
# def test_should_return_two_when_ages_are_equal_second_year():
#     assert get_human_age(24, 24) == [2, 2]
#
#
# def test_should_return_two_when_ages_are_below_third_year():
#     assert get_human_age(27, 28) == [2, 2]


# def test_should_return_three_when_ages_are_equal_third_year():
#     assert get_human_age(28, 29) == [3, 3]
#
#
# def test_should_return_correct_value_when_ages_are_bigger_than_third_year():
#     assert get_human_age(100, 100) == [21, 17]
