import pytest
from typing import Any
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result_convert_to_human_age",
        [
            pytest.param(0, 0, [0, 0],
                         id="when input is 0"),
            pytest.param(-14, -15, [0, 0],
                         id="when input is negative"),
            pytest.param(14, 14, [0, 0],
                         id="should convert to 0 if age less then 15"),
            pytest.param(15, 15, [1, 1],
                         id="should convert to 1 if age 15"),
            pytest.param(23, 23, [1, 1],
                         id="should convert to 1 if age less then 24"),
            pytest.param(24, 24, [2, 2],
                         id="should convert to 2 if age 24"),
            pytest.param(27, 28, [2, 2],
                         id="should convert to 2 if age less then 27 and 28"),
            pytest.param(28, 29, [3, 3],
                         id="should convert to 3 if age more then 28 and 29"),

        ]
    )
    def test_calculate_human_age(
            self,
            cat_age: int,
            dog_age: int,
            result_convert_to_human_age: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result_convert_to_human_age

    @pytest.mark.parametrize("cat_age, dog_age", [
        pytest.param("5", 5),
        pytest.param(5, "5"),
        pytest.param("5", "5")
    ])
    def test_incorrect_type_param(self,
                                  cat_age: Any,
                                  dog_age: Any) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
