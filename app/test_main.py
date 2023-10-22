from typing import Any, Type

import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_age",
        [
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
            (-5, 1, [0, 0]),
            (16.5, 28.1, [1, 2]),
            (0, 0, [0, 0])
        ]
    )
    def test_get_human_age(
            self,
            cat_age: Any,
            dog_age: Any,
            expected_age: Any
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_age

    @pytest.mark.parametrize(
        "cat_age, dog_age, error",
        [
            ((), (), TypeError),
            ({28}, [], TypeError),
            ([28, 4], (28, 1), TypeError)
        ]
    )
    def test_get_human_age_invalid_error(
            self,
            cat_age: Any,
            dog_age: Any,
            error: Type[Exception]
    ) -> None:
        with pytest.raises(error):
            get_human_age(cat_age, dog_age)
