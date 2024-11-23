from app.main import get_human_age


class TestGetHumanAge:
    def test_get_human_age_24_24(self) -> None:
        cat_age = 24
        dog_age = 24
        result = get_human_age(cat_age=cat_age, dog_age=dog_age)
        assert result == [2, 2], "Result should be [2, 2]"

    def test_get_human_age_14_14(self) -> None:
        cat_age = 14
        dog_age = 14
        result = get_human_age(cat_age=cat_age, dog_age=dog_age)
        assert result == [0, 0], "Result should be [0, 0]"

    def test_get_human_age_15_15(self) -> None:
        cat_age = 15
        dog_age = 15
        result = get_human_age(cat_age=cat_age, dog_age=dog_age)
        assert result == [1, 1], "Result should be [1, 1]"

    def test_get_human_age_23_23(self) -> None:
        cat_age = 23
        dog_age = 23
        result = get_human_age(cat_age=cat_age, dog_age=dog_age)
        assert result == [1, 1], "Result should be [1, 1]"

    def test_get_human_age_27_28(self) -> None:
        cat_age = 27
        dog_age = 28
        result = get_human_age(cat_age=cat_age, dog_age=dog_age)
        assert result == [2, 2], "Result should be [2, 2]"

    def test_get_human_age_28_29(self) -> None:
        cat_age = 28
        dog_age = 29
        result = get_human_age(cat_age=cat_age, dog_age=dog_age)
        assert result == [3, 3], "Result should be [3, 3]"
