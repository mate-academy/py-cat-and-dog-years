import pytest
from app.main import get_human_age


class TestGetHumanAge:
    def test_animal_age_if_animal_human_age_less_than_15(self) -> None:
        assert get_human_age(0, 0) == [0, 0]
        assert get_human_age(14, 14) == [0, 0]

    def test_animal_age_if_animal_human_age_is_15_or_more(self) -> None:
        assert get_human_age(15, 15) == [1, 1]
        assert get_human_age(23, 23) == [1, 1]
        assert get_human_age(24, 24) == [2, 2]
        assert get_human_age(27, 27) == [2, 2]
        assert get_human_age(28, 28) == [3, 2]
        assert get_human_age(100, 100) == [21, 17]

    def test_negative_attributes_passed(self) -> None:
        assert get_human_age(-1, -1) == [0, 0]
        assert get_human_age(15, -1) == [1, 0]
        assert get_human_age(-1, 15) == [0, 1]


class TestInvalidInput:
    def test_raise_other_type_of_attribute(self) -> None:
        with pytest.raises(TypeError):
            assert get_human_age("", 15)
            assert get_human_age(15, "")
            assert get_human_age("", "")