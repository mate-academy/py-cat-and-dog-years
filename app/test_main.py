from typing import Type

import pytest

from app.main import get_human_age


class TestGetHumanAge:
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
            (100, 100, [21, 17])
        ]
    )
    def test_get_human_age_with_correct_values(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            ("value", 12, TypeError),
            (13, "value", TypeError)
        ]
    )
    def test_get_human_age_with_correct_types_of_value(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Type[BaseException]
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
