import pytest
from typing import Any
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(
                -1,
                -1,
                [0, 0],
                id="should return zeros if ages is negative numbers",
            ),
            pytest.param(
                0,
                0,
                [0, 0],
                id="should return zeros if ages is zeros",
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="14 cat/dog years should convert into 0 human age",
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="23 cat/dog years should convert into 1 human age",
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="24 cat/dog years should convert into 2 human age",
            ),
            pytest.param(
                27,
                28,
                [2, 2],
                id="27/28 cat/dog years should convert into 2 human age",
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="28/29 cat/dog years should convert into 3 human age",
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="100 cat/dog years should convert into 21/17 human age",
            ),
        ],
    )
    def test_return_correct_age(
        self, cat_age: int, dog_age: int, expected_result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_error",
        [
            pytest.param(
                [],
                5,
                TypeError,
                id="should raise TypeError if age is not integer",
            ),
        ],
    )
    def test_raising_errors_correctly(
        self, cat_age: int, dog_age: int, expected_error: Any
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
