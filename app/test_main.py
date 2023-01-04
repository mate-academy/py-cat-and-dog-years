import pytest

from typing import Any
from app.main import get_human_age


class TestCheckAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
        [
            pytest.param(
                -2, -2,
                [0, 0],
                id="human age should be 0, if pet age is negative"
            ),
            pytest.param(
                0, 0,
                [0, 0],
                id="human age should be 0, if pet age is 0"
            ),
            pytest.param(
                14, 14,
                [0, 0],
                id="14 cat/dog years should convert into 0 human age."
            ),
            pytest.param(
                23, 23,
                [1, 1],
                id="23 cat/dog years should convert into 1 human age."
            ),
            pytest.param(
                27, 28,
                [2, 2],
                id="27/28 cat/dog years should convert into 2 human age."
            ),
            pytest.param(
                28, 29,
                [3, 3],
                id="28/29 cat/dog years should convert into 3 human age."
            ),
            pytest.param(
                100, 100,
                [21, 17],
                id="100 cat/dog years should convert into 23/17 human age."
            )
        ]
    )
    def test_correct_output(
            self,
            cat_age: Any,
            dog_age: Any,
            expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected
        assert isinstance(expected[0] and expected[1], int)

    @pytest.mark.parametrize(
        "cat_age,dog_age",
        [
            pytest.param(
                "1", "1",
                id="if ages are string"
            )
        ]
    )
    def test_should_raise_type_error_if_age_is_string(
            self,
            cat_age: Any,
            dog_age: Any
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
