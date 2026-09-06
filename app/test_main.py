import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            pytest.param(0, 0, [0, 0], id="1_1"),
            pytest.param(14, 14, [0, 0], id="14_14"),
            pytest.param(15, 15, [1, 1], id="15_15"),
            pytest.param(23, 23, [1, 1], id="23_23"),
            pytest.param(24, 24, [2, 2], id="24_24"),
            pytest.param(27, 27, [2, 2], id="27_27"),
            pytest.param(28, 28, [3, 2], id="28_28"),
            pytest.param(100, 100, [21, 17], id="100_100"),
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result

    @pytest.mark.parametrize(
        "cat_age, dog_age, exepted_error",
        [
            pytest.param(-2, 0, ValueError, id="negative numbers"),
            pytest.param("two", "hello", TypeError, id="wrong type")
        ]
    )
    def test_get_human_age_errors(
            self,
            cat_age: int,
            dog_age: int,
            exepted_error: Exception
    ) -> None:
        with pytest.raises(exepted_error):
            get_human_age(cat_age, dog_age)
