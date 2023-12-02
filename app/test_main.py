import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            (0, 0, [0, 0]),
            (10, 10, [0, 0]),
            (14, 14, [0, 0])
        ]
    )
    def test_input_age_less_than_one_year_human(self, cat_age, dog_age, expected_result):
        assert get_human_age(cat_age, dog_age) == expected_result

    def test_input_age_equal_one_year_human(self):
        assert get_human_age(15, 15) == [1, 1]
        assert get_human_age(23, 23) == [1, 1]

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (27, 28, [2, 2])
        ]
    )
    def test_input_age_equal_two_years_human(self, cat_age, dog_age, expected_result):
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            (28, 29, [3, 3]),
            (50, 55, [8, 8]),
            (73, 78, [14, 12]),
            (100, 100, [21, 17])
        ]
    )
    def test_input_age_bigger_than_two_years_human(self, cat_age, dog_age, expected_result):
        assert get_human_age(cat_age, dog_age) == expected_result
