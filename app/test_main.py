import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_ages",
        [
            pytest.param(0, 0, [0, 0], id="zero years should return zero human year"),
            pytest.param(14, 14, [0, 0], id="4 years should return zero human years"),
            pytest.param(15, 15, [1, 1], id="zero years should return zero human year"),
            pytest.param(23, 23, [1, 1], id="under second milestone discards remainder"),
            pytest.param(24, 24, [2, 2], id="twenty four years should return two human years"),
            pytest.param(27, 0, [2, 0], id="cat remainder handling"),
            pytest.param(0, 28, [0, 2], id="dog remainder handling"),
            pytest.param(28, 0, [3, 0], id="cat scaling after 24"),
            pytest.param(0, 29, [0, 3], id="dog scaling after 24"),
            pytest.param(40, 44, [6, 6], id="both animals scaling simultaneously"),
        ]
    )
    def test_returns_correct_age(self, cat_age, dog_age, human_ages):
        assert get_human_age(cat_age,dog_age) == human_ages

    # def test_zero_years_should_return_zero_human_years(self):
    #     assert get_human_age(0,0) == [0, 0]
    #
    # def test_14_years_should_return_zero_human_years(self):
    #     assert get_human_age(14,14) == [0, 0]
    #
    # def test_fifteen_years_should_return_one_human_year(self):
    #     assert get_human_age(15,15) == [1, 1]
    #
    # def test_under_second_milestone_discards_remainder(self):
    #     assert get_human_age(23, 23) == [1, 1]
    #
    # def test_twenty_four_years_should_return_two_human_years(self):
    #     assert get_human_age(24,24) == [2, 2]
    #
    # def test_cat_remainder_handling(self):
    #     assert get_human_age(27, 0) == [2, 0]
    #
    # def test_dog_remainder_handling(self):
    #     assert get_human_age(0, 28) == [0, 2]
    #
    # def test_cat_scaling_after_24(self):
    #     assert get_human_age(28, 0) == [3, 0]
    #
    # def test_dog_scaling_after_24(self):
    #     assert get_human_age(0, 29) == [0, 3]
    #
    # def test_both_animals_scaling_simultaneously(self):
    #     assert  get_human_age(40, 44) == [6, 6]