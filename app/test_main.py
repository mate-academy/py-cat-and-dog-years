from app.main import get_human_age


class TestGetHumanAge:
    def test_convert_age_if_animal_age_is_0(self):
        goals = get_human_age(0, 0)
        assert goals == [0, 0]

    def test_convert_age_if_animal_age_closely_to_first_human_year(self):
        goals = get_human_age(0, 0)
        assert goals == [0, 0]

    def test_convert_age_if_animal_age_between_1_and_2_human_age(self):
        goals = get_human_age(18, 18)
        assert goals == [1, 1]

    def test_convert_age_if_animal_age_closely_to_second_human_year(self):
        goals = get_human_age(23, 23)
        assert goals == [1, 1]

    def test_convert_age_if_animal_age_equal_2_human_year(self):
        goals = get_human_age(24, 24)
        assert goals == [2, 2]

    def test_convert_age_if_animal_age_closely_to_third_human_year(self):
        goals = get_human_age(27, 27)
        assert goals == [2, 2]

    def test_convert_age_if_animals_age_have_different_human_age(self):
        goals = get_human_age(28, 28)
        assert goals == [3, 2]

    def test_convert_age_if_animal_age_very_big(self):
        goals = get_human_age(100, 100)
        assert goals == [21, 17]
