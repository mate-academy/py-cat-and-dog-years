from app.main import get_human_age
import pytest
from typing import Any


class TestValues:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_value",
        [
            pytest.param(
                15,
                15,
                [1, 1],
                id="Correct values for 15, 15"),
            pytest.param(
                24,
                24,
                [2, 2],
                id="Correct values for, 24, 24"),
            pytest.param(
                28,
                29,
                [3, 3],
                id="Correct values for 28, 29"),
            pytest.param(
                0,
                0,
                [0, 0],
                id="Return 0 when animal age is 0"),
            pytest.param(
                100.5,
                100.5,
                [21, 17],
                id="Test for big and fractional numbers"),
            pytest.param(
                -15,
                -20,
                [0, 0],
                id="Test for negative numbers"),
        ]
    )
    def test_should_return_correct_values(
            self,
            cat_age: int,
            dog_age: int,
            expected_value: list) -> None:
        assert get_human_age(cat_age, dog_age) == expected_value

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                "string",
                "string",
                TypeError,
                id="Raise 'TypeError' error for string"),
        ]
    )
    def test_should_return_type_error(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Any) -> Any:
        with pytest.raises(expected_error):
            assert get_human_age(cat_age, dog_age)
