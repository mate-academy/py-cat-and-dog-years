from app.main import get_human_age


class TestHumanAge:

    def test_get_human_age_animal_age_younger_one(self):
        assert get_human_age(10, 10) == [0, 0]

    def test_get_human_age_animal_age_elder_one(self):
        assert get_human_age(16, 16) == [1, 1]

    def test_get_human_age_animal_very_old(self):
        assert get_human_age(100, 100) == [21, 17]
