import pytest

from app.main import get_human_age


class TestForWorkingCases:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (31, 35, [3, 4]),
            (100, 100, [21, 17])
        ]
    )
    def test_to_get_correct_result(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result


class TestForErrors:
    def test_incorrect_type_string(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("28", "28")

    def test_incorrect_type_float(self) -> None:
        with pytest.raises(TypeError):
            get_human_age(15.5, 28.3)

    def test_incorrect_type_negative(self) -> None:
        with pytest.raises(ValueError):
            get_human_age(-14, -28)
