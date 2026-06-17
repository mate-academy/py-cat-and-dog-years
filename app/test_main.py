from app.main import get_human_age


# write your code here
class TestGetHumanAge:
    def test_should_return_0_when_(self) -> None:
        assert get_human_age(0, 0) == [0, 0]

    def test_should_return_0_when_age_lower_than_15(self) -> None:
        assert get_human_age(14, 14) == [0, 0]

    def test_should_return_1_when_age_is_15(self) -> None:
        assert get_human_age(15, 15) == [1, 1]

    def test_should_count_right_when_age_lower_than_24(self) -> None:
        assert get_human_age(23, 23) == [1, 1]

    def test_should_count_right_when_age_is_24(self) -> None:
        assert get_human_age(24, 24) == [2, 2]

    def test_should_count_right_when_age_between_24_and_higher(self) -> None:
        assert get_human_age(27, 27) == [2, 2]

    def test_should_count_right_cat_and_dog_formula_on_age_higher_27(
            self
    ) -> None:
        assert get_human_age(28, 28) == [3, 2]

    def test_should_work_with_big_args(self) -> None:
        assert get_human_age(100, 100) == [21, 17]
