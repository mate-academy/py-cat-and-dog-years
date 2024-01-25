from app.main import get_human_age


class TestGetHumanAge:
    def test_return_list_with_zeros_when_less_first_years(self) -> None:
        assert get_human_age(10, 10) == [0, 0]

    def test_return_list_with_ones_when_less_first_second_years_sum(
        self
    ) -> None:
        assert get_human_age(21, 19) == [1, 1]

    def test_correct_calculating_years(self) -> None:
        assert get_human_age(32, 46) == [4, 6]
