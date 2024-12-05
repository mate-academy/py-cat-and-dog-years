import pytest

from app.main import get_human_age


class TestGetHumanAge:
    def test_should_be_equal_zero(self) -> None:
        assert get_human_age(0, 0) == [0, 0]
        assert get_human_age(3, 2) == [0, 0]
        assert get_human_age(12, 4) == [0, 0]
        assert get_human_age(14, 14) == [0, 0]

    def test_should_be_equal_one(self) -> None:
        assert get_human_age(17, 17) == [1, 1]
        assert get_human_age(18, 2) == [1, 0]
        assert get_human_age(19, 23) == [1, 1]
        assert get_human_age(2, 23) == [0, 1]

    def test_should_be_result_function(self) -> None:
        assert get_human_age(35, 30) == [4, 3]
        assert get_human_age(60, 60) == [11, 9]
        assert get_human_age(70, 65) == [13, 10]
        assert get_human_age(105, 105) == [22, 18]
        assert get_human_age(120, 120) == [26, 21]

    def test_should_type_error(self) -> None:
        with pytest.raises(TypeError):
            get_human_age(5, "5")
