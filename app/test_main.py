from app.main import get_human_age


class TestGetHumanAge:
    def test_animals_age_equal_0(self) -> None:
        cat_age, dog_age = 0, 0
        result = get_human_age(cat_age, dog_age)
        assert result == [0, 0]

    def test_animals_age_less_15(self) -> None:
        cat_age, dog_age = 14, 14
        result = get_human_age(cat_age, dog_age)
        assert result == [0, 0]

    def test_animals_age_less_24_bigger_15(self) -> None:
        cat_age, dog_age = 23, 23
        result = get_human_age(cat_age, dog_age)
        assert result == [1, 1]

    def test_cat_age_bigger_28(self) -> None:
        cat_age, dog_age = 28, 27
        result = get_human_age(cat_age, dog_age)
        assert result == [3, 2]

    def test_animals_age_bigger_99(self) -> None:
        cat_age, dog_age = 100, 100
        result = get_human_age(cat_age, dog_age)
        assert result == [21, 17]

    def test_animals_age_bigger_999(self) -> None:
        cat_age, dog_age = 1000, 1000
        result = get_human_age(cat_age, dog_age)
        assert result == [246, 197]
