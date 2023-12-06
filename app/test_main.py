import pytest

from app.main import get_human_age
from typing import Any



class TestGetHumanAge:
    @pytest.mark.parametrize(
        "initial_cat_age, initial_dog_age, expected_result",
        [
            pytest.param(
                0, 0, [0, 0],
                id="test should return zero when age is zero"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="test should return zero when age is less then 15"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="test should return one when age is equal "
                   "or more then 15 and less then 24"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="test should return two when age is equal "
                   "or more then 24 and less then 28 for cat or 29 for dog"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="test should return different values when age is "
                   "more then 27 for cat and more then 28 for dog"
            ),
            pytest.param(
                -4, -3, [0, 0],
                id="test should return zero when "
                   "age is less then zero"
            ),
            pytest.param(
                1000, 502, [246, 97],
                id="test should return correct value"
            ),
        ]
    )
    def test_get_human_age(
            self,
            initial_cat_age: int,
            initial_dog_age: int,
            expected_result: list[int]
    ) -> None:
        assert get_human_age(initial_cat_age, initial_dog_age) == expected_result

    @pytest.mark.parametrize(
        "initial_cat_age,initial_dog_age,expected_error",
        [
            pytest.param(
                "5", "5",
                TypeError,
                id="should raise error when age is 'str'"
            ),
            pytest.param(
                {}, 5,
                TypeError,
                id="should raise error when age is 'dict'"
            ),pytest.param(
                5, [],
                TypeError,
                id="should raise error when age is not 'list'"
            ),
            pytest.param(
                (), "5",
                TypeError,
                id="should raise error when age is not 'tuple'"
            ),
            pytest.param(
                5, set(),
                TypeError,
                id="should raise error when age is not 'set'"
            )
        ]
    )
    def test_raising_errors_correctly(
            self,
            initial_cat_age: Any,
            initial_dog_age: Any,
            expected_error: TypeError
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(initial_cat_age, initial_dog_age)
