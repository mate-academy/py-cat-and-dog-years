import pytest

from app.main import get_human_age


class TestPetsHumanAge:
    def test_should_params_be_int_not_str(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("15", "15"), "parameters must be an integer, not str"

    def test_should_convert_negative_years_to_0(self) -> None:
        assert get_human_age(-5, -15) == [0, 0], \
            "negative years should convert into 0 human age."

    def test_should_convert_0_to_0(self) -> None:
        assert get_human_age(0, 0) == [0, 0], \
            "0 years should convert into 0 human age."

    def test_should_convert_before_15_year_to_0(self) -> None:
        assert get_human_age(14, 14) == [0, 0], \
            "1-14 years should convert into 0 human age."

    def test_should_convert_15_year_to_1(self) -> None:
        assert get_human_age(15, 15) == [1, 1], \
            "15 years should convert into 1 human age."

    def test_should_convert_between_15_and_24_year_to_1(self) -> None:
        assert get_human_age(23, 23) == [1, 1], \
            "from 15 up to 24 years should convert into 1 human age."

    def test_should_convert_24_year_to_2(self) -> None:
        assert get_human_age(24, 24) == [2, 2], \
            "24 years should convert into 2 human age."

    def test_should_convert_over_24_year_border(self) -> None:
        assert get_human_age(27, 28) == [3, 3], \
            "27/28 years should convert into 3 human age."

    def test_should_convert_over_24_year_without_rounding(self) -> None:
        assert get_human_age(28, 29) == [3, 3], \
            "28/29 years should convert into 3 human age."

    def test_should_convert_over_24_year_with_rounding(self) -> None:
        assert get_human_age(37, 41) == [5, 5], \
            "37/41 years should convert into 5 human age."

    def test_should_convert_incredible_years(self) -> None:
        assert get_human_age(100, 100) == [21, 17], \
            "100/100 years should convert into 21/17 human age."
