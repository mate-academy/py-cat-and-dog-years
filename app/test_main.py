import pytest

from app.main import get_human_age


class TestGetHumanAge:
    def test_should_raise_error(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("4", [1, 4])

    def test_if_pets_age_less_than_zero(self) -> None:
        assert get_human_age(-1, -2) == [0, 0]

    def test_if_pets_age_zero(self) -> None:
        assert get_human_age(0, 0) == [0, 0]

    def test_if_pets_age_less_15(self) -> None:
        assert get_human_age(14, 14) == [0, 0]

    def test_if_pets_age_15_years(self) -> None:
        assert get_human_age(15, 15) == [1, 1]

    def test_if_pets_age_15_and_24_years(self) -> None:
        assert get_human_age(23, 23) == [1, 1]
        assert get_human_age(24, 24) == [2, 2]

    def test_if_pets_age_between_25_and_27_years(self) -> None:
        assert get_human_age(25, 25) == [2, 2]
        assert get_human_age(27, 27) == [2, 2]

    def test_if_pets_age_over_27_years(self) -> None:
        assert get_human_age(28, 28) == [3, 2]
        assert get_human_age(100, 100) == [21, 17]
