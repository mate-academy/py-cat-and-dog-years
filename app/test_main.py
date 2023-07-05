from app.main import get_human_age


class TestGetHumanAge:
    def test_no_arguments(self) -> None:
        assert get_human_age(0, 0) == [0, 0]

    def test_less_one_year(self) -> None:
        assert get_human_age(14, 14) == [0, 0]

    def test_one_year(self) -> None:
        assert get_human_age(15, 15) == [1, 1]

    def test_second_years(self) -> None:
        assert get_human_age(23, 23) == [1, 1]

    def test_two_years(self) -> None:
        assert get_human_age(24, 24) == [2, 2]

    def test_three_years(self) -> None:
        assert get_human_age(28, 29) == [3, 3]

    def test_cat_three_dog_end_of_second(self) -> None:
        assert get_human_age(28, 28) == [3, 2]

    def test_old_cat_and_dog(self) -> None:
        assert get_human_age(100, 100) == [21, 17]
