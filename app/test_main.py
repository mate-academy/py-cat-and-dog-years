from app.main import get_human_age
import pytest
from typing import Any


class TestsGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age_input, dog_age_input, expected_age",
        [
            pytest.param(
                0, 0, [0, 0],
                id="should return [0, 0]"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="should return [0, 0]"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="should return [1, 1]"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="should return [1, 1]"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="should return [2, 2]"
            ),
            pytest.param(
                27, 27, [2, 2],
                id="should return [2, 2]"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="should return [21, 17]"),

        ]
    )
    def test_program(
            self,
            cat_age_input: int,
            dog_age_input: int,
            expected_age: list
    ) -> None:
        assert get_human_age(cat_age_input, dog_age_input) == expected_age

    @pytest.mark.parametrize(
        "cat_age_input, dog_age_input, expected_error",
        [
            pytest.param(
                "1", 1, TypeError,
                id="type cat_age_input and dog_age_input is int"
            )
        ]
    )
    def test_raise_errors(
            self,
            cat_age_input: int,
            dog_age_input: int,
            expected_error: Any
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age_input, dog_age_input)
