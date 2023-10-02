from typing import Type
import pytest
from app.main import get_human_age


class TestConvertInHumanAge:
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
            (-100, -100, [0, 0]),
            (10**9, 10**9, [249999996, 199999997]),
        ],
    )
    def test_right_conversion_in_human_age(
        self, cat_age: int, dog_age: int, expected_result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [("value", 13, TypeError), (13, "value", TypeError)],
    )
    def test_age_conversion_with_wrong_age_type(
        self, cat_age: int, dog_age: int, expected_result: Type[BaseException]
    ) -> None:
        with pytest.raises(expected_result):
            get_human_age(cat_age, dog_age)
