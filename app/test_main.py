import pytest
from app.main import get_human_age
from typing import Any


class TestCatDogYears:
    @pytest.mark.parametrize(
        "initial_values, expected_outcome",
        [
            pytest.param(
                (0, -15), [0, 0],
                id="should return zeros if initial "
                   "values are less or equal to 0"),
            pytest.param(
                (15, 15), [1, 1],
                id="should return ones if cat and dog age equals to 15"),
            pytest.param(
                (24, 24), [2, 2],
                id="should return twos if cat and dog age equals to 24"),
            pytest.param(
                (28, 28), [3, 2],
                id="test should return different values "
                   "if cat and dog age equals to 28"),
            pytest.param(
                (100, 100), [21, 17],
                id="test check with large number")
        ]
    )
    def test_should_return_correct_outcome(
        self,
        initial_values: tuple,
        expected_outcome: list
    ) -> None:
        result = get_human_age(*initial_values)

        assert result == expected_outcome

    @pytest.mark.parametrize(
        "initial_values, expected_error",
        [
            pytest.param(
                ("15", "24"), TypeError,
                id="should raise error if ages are of str type"
            ),
            pytest.param(
                (), TypeError,
                id="should raise error when no argument provided"
            )
        ]
    )
    def test_should_raise_correct_errors(
            self,
            initial_values: tuple,
            expected_error: Any
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(*initial_values)
