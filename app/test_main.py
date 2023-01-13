import pytest
from app.main import get_human_age
from typing import Any


class TestGetHumanAge:

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            pytest.param(
                23,
                23,
                [1, 1],
                id="should work when data value is in normal range"
            ),
            pytest.param(
                22,
                22,
                [1, 1],
                id="output must not be changed with the previous value"
            ),
            pytest.param(
                0,
                0,
                [0, 0],
                id="should work when data value is zero"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="should work with large numbers"
            ),
            pytest.param(
                -1,
                -2,
                [0, 0],
                id="should work with negative numbers"
            ),
        ]
    )
    def test_interpret_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param("14",
                         14,
                         TypeError,
                         id="should raise error when data type is not int")
        ]
    )
    def test_raise_errors_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Any
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
