import pytest
from typing import Any
from app import main


class TestCatAndDogYearsInHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_human_age",
        [
            (-10, -10, [0, 0]),
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (14, 15, [0, 1]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (23, 24, [1, 2]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 15, [3, 1]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
            (1000, 1000, [246, 197]),
        ],
        ids=[
            "Negative numbers",
            "Zeros",
            "Fourteen",
            "Fourteen and fifteen",
            "Fifteen",
            "Twenty three",
            "Twenty three and twenty four",
            "Twenty four",
            "Twenty seven",
            "Twenty eight and fifteen",
            "Twenty eight",
            "One hundred",
            "Big numbers"
        ]
    )
    def test_cat_dog_years_in_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected_human_age: list
    ) -> None:
        assert (
            main.get_human_age(cat_age, dog_age) == expected_human_age
        ), f"{cat_age} and {dog_age} should return {expected_human_age}"

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                "10",
                10,
                TypeError,
                id="Value should be integers"
            ),
            pytest.param(
                [10],
                10,
                TypeError,
                id="Value should not be list"
            ),
            pytest.param(
                10,
                None,
                TypeError,
                id="Value cannot be None"
            )
        ]
    )
    def test_raising_errors_correctly(
            self,
            cat_age: Any,
            dog_age: Any,
            expected_error: type[Exception]
    ) -> None:
        with pytest.raises(expected_error):
            main.get_human_age(cat_age, dog_age)
