import pytest
from typing import Any
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            pytest.param(
                -1, -1, [0, 0],
                id="Human age should be equal to 0 when pet age is negative"
            ),
            pytest.param(
                0, 0, [0, 0],
                id="Human age should be equal to 0 when pet age < 15"
            ),
            pytest.param(
                20, 20, [1, 1],
                id="Human age should be equal to 1 when 15 <= pet age < 24"
            ),
            pytest.param(
                27, 27, [2, 2],
                id="Human age should be equal to 2 when 24 <= pet age < 27"
            ),
            pytest.param(
                28, 29, [3, 3],
                id="28/29 cat/dog years should convert into 3 human age."
            ),
            pytest.param(
                100, 100, [21, 17],
                id="100 cat/dog years should convert into 21/17 human age."
            ),

        ]
    )
    def test_correct_output(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list
    ) -> None:
        assert (get_human_age(cat_age, dog_age) == expected_result)

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ("1", 1),
            (1, "1"),
            ("1", "1")
        ]

    )
    def test_incorrect_type_error(self, cat_age: Any, dog_age: Any) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
