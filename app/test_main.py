from app.main import get_human_age


class TestGetHumanAge:

    def test_get_human_age_if_age_of_animal_is_zero(self):
        assert get_human_age(14, 14) == [0, 0]

    def test_get_human_age_if_age_of_animal_is_one(self):
        assert get_human_age(15, 15) == [1, 1]

    def test_get_human_age_if_age_of_animal_is_two(self):
        assert get_human_age(24, 24) == [2, 2]

    def test_get_human_age_if_age_of_animal_more_or_equal_three(self):
        assert get_human_age(28, 29) == [3, 3]
