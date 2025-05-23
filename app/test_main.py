from app.main import get_human_age, convert_to_human


class TestConvertToHuman:
    def test_method_parametrs_should_be_integer(self) -> None:
        result = convert_to_human(30, 15, 9, 4)
        assert isinstance(result, int)

    def test_method_animal_age_less_first_year_equal_zero(self) -> None:
        result = convert_to_human(10, 15, 9, 4)
        assert result == 0

    def test_method_animal_age_less_first_and_second_equal_one(self) -> None:
        result = convert_to_human(15, 10, 8, 2)
        assert result == 1

    def test_cat_30_years_should_return_4_human_years(self) -> None:
        result = convert_to_human(30, 15, 9, 4)
        assert result == 3  # 2 + (30 - 15 - 9)//4 = 2 + 6//4 = 2 + 1 = 3


class TestGetHumanAge:
    def test_method_get_human_age_should_return_list(self) -> None:
        result = get_human_age(3, 2)
        assert isinstance(result, list)

    def test_should_return_correct_for_23_years(self) -> None:
        assert get_human_age(23, 23) == [1, 1]

    def test_should_return_correct_for_24_years(self) -> None:
        assert get_human_age(24, 24) == [2, 2]

    def test_should_return_correct_for_28_years(self) -> None:
        assert get_human_age(28, 28) == [3, 2]

    def test_should_return_correct_for_zero_ages(self) -> None:
        assert get_human_age(0, 0) == [0, 0]

    def test_should_return_correct_for_min_thresholds(self) -> None:
        assert get_human_age(15, 15) == [1, 1]

    def test_should_return_correct_larger_numbers(self) -> None:
        assert get_human_age(100, 100) == [21, 17]
