import pytest
from typing import Any
from app.main import get_human_age


class TestGetHumanAge:

    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (23, 23, [1, 1]),
            (100, 100, [21, 17]),
            (-2, -5, [0, 0])
        ],
        ids=[
            "0 cat/dog years should convert into 0 human age.",
            "14 cat/dog years should convert into 0 human age.",
            "23 cat/dog years should convert into 1 human age.",
            "100 cat/dog years should convert into 21/17 human age.",
            "negative numbers should convert into 0 human age.",
        ]
    )
    def test_human_age_calculated_correctly(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                "zero",
                "zero",
                TypeError,
                id="should raise error when age not integer"
            ),
        ]
    )
    def test_raising_error_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Any
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
