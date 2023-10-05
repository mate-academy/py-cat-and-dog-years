from app.main import get_human_age


class TestGetHumanAgeClass:
    def test_human_age_when_cat_and_dog_age_are_14(self) -> None:
        assert get_human_age(14, 14) == [0, 0]

    def test_human_age_when_cat_and_dog_age_are_24(self) -> None:
        assert get_human_age(24, 24) == [2, 2]

    def test_human_age_when_cat_age_27_and_dog_age_28(self) -> None:
        assert get_human_age(27, 28) == [2, 2]

    def test_human_age_when_cat_age_28_and_dog_age_29(self) -> None:
        assert get_human_age(28, 29) == [3, 3]
