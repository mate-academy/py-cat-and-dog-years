from app.main import get_human_age
import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            pytest.param(0, 0, [0, 0]),
            pytest.param(14, 14, [0, 0]),
            pytest.param(15, 15, [1, 1]),
            pytest.param(23, 23, [1, 1]),
            pytest.param(24, 24, [2, 2]),
            pytest.param(27, 27, [2, 2]),
            pytest.param(28, 28, [3, 2]),
            pytest.param(100, 100, [21, 17]),
        ]
    )
    def test_conversion_to_human_years(
            self, cat_age: int, dog_age: int, result: list) -> None:
        assert get_human_age(cat_age, dog_age) == result

    def test_invalid_data_types_raise_exception(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("not_an_integer", 10)

        with pytest.raises(TypeError):
            get_human_age(5, "not_an_integer")

        with pytest.raises(TypeError):
            get_human_age("not_an_integer", "not_an_integer")
