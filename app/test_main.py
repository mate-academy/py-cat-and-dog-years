import pytest
from typing import Any
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_age",
        [
            pytest.param(
                -1, -2, [0, 0],
                id="years should be positive integers."
            ),
            pytest.param(
                0, 0, [0, 0],
                id="years should convert into 0 human age."
            ),
            pytest.param(
                14, 14, [0, 0],
                id="years should convert into 0 human age."
            ),
            pytest.param(
                15, 15, [1, 1],
                id="years should convert into 1 human age."
            ),
            pytest.param(
                23, 23, [1, 1],
                id="years should convert into 1 human age."
            ),
            pytest.param(
                24, 24, [2, 2],
                id="years should convert into 2 human age."
            ),
            pytest.param(
                28, 29, [3, 3],
                id="years should convert into 3 human age."
            )
        ]
    )
    def test_modify_age_correctly(
        self,
        cat_age: int,
        dog_age: int,
        expected_age: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_age

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                2.1, [2], TypeError,
                id="should raise error when age cat/dog is not integer"
            )
        ]
    )
    def test_raising_error_correctly(
        self,
        cat_age: Any,
        dog_age: Any,
        expected_error: Any
    ) -> None:

        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
