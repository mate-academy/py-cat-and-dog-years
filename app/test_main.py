from app.main import get_human_age
from typing import Any
import pytest


class TestHumanAge:
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
            (50, 50, [8, 7]),
            (-1, -1, [0, 0]),
        ]
    )
    def test_correct_human_age(self, cat_age: int, dog_age: int, expected_result: int) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age,dog_age",
        [
            ("1", "1"),
            ([], []),
        ]
    )
    def test_raises_error_when_wrong_data(self, cat_age: Any, dog_age: Any) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
