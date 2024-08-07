from app.main import get_human_age


def test_get_human_age_zero_years() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]


class TestCatYearsToHumanYears:
    def test_cat_age_0(self) -> None:
        assert get_human_age(0, 0)[0] == 0

    def test_cat_age_14(self) -> None:
        assert get_human_age(14, 0)[0] == 0

    def test_cat_age_15(self) -> None:
        assert get_human_age(15, 0)[0] == 1

    def test_cat_age_23(self) -> None:
        assert get_human_age(23, 0)[0] == 1

    def test_cat_age_24(self) -> None:
        assert get_human_age(24, 0)[0] == 2

    def test_cat_age_27(self) -> None:
        assert get_human_age(27, 0)[0] == 2

    def test_cat_age_28(self) -> None:
        assert get_human_age(28, 0)[0] == 3

    def test_cat_age_100(self) -> None:
        assert get_human_age(100, 0)[0] == 21


class TestDogYearsToHumanYears:
    def test_dog_age_0(self) -> None:
        assert get_human_age(0, 0)[1] == 0

    def test_dog_age_14(self) -> None:
        assert get_human_age(0, 14)[1] == 0

    def test_dog_age_15(self) -> None:
        assert get_human_age(0, 15)[1] == 1

    def test_dog_age_23(self) -> None:
        assert get_human_age(0, 23)[1] == 1

    def test_dog_age_24(self) -> None:
        assert get_human_age(0, 24)[1] == 2

    def test_dog_age_27(self) -> None:
        assert get_human_age(0, 27)[1] == 2

    def test_dog_age_28(self) -> None:
        assert get_human_age(0, 28)[1] == 2

    def test_dog_age_100(self) -> None:
        assert get_human_age(0, 100)[1] == 17
