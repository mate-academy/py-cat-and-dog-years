from app.main import get_human_age
import pytest
from typing import Any


class TestGetHumanAge:

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
            (24, 23, [2, 1]),
            (-24, -23, [0, 0])
        ],
    )
    def test_should_check_return_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age,dog_age",
        [
            ("24", 24),
            (24, "24"),
            ("24", "24"),
            (None, 24),
            (24, None),
            (None, None),
            ([24], [24])
        ]
    )
    def test_should_accept_correct_types(
            self, cat_age: Any, dog_age: Any
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
