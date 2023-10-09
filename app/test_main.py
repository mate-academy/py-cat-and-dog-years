import pytest
from typing import Any, Type
from app.main import get_human_age


class TestCatDogInHumanYearsClass:
    @pytest.mark.parametrize(
        "initial_years, expected_years",
        [
            pytest.param(
                (-1, -1),
                [0, 0],
                id="should return zero if initial years are less than 0"
            ),
            pytest.param(
                (0, 0),
                [0, 0],
                id="should return 0 if initial years are equal 0"
            ),
            pytest.param(
                (14, 14),
                [0, 0],
                id="should return 0 if initial years are less than or equal to 14"
            ),
            pytest.param(
                (15, 15),
                [1, 1],
                id="should return 1 if initial years are equal 15"
            ),
            pytest.param(
                (23, 23),
                [1, 1],
                id="should return 1 if initial years are equal 23"
            ),
            pytest.param(
                (24, 24),
                [2, 2],
                id="should return 2 if initial years are equal 23"
            ),
            pytest.param(
                (27, 27),
                [2, 2],
                id="should return 2 if initial years are equal 27"
            ),
            pytest.param(
                (28, 28),
                [3, 2],
                id="should return different expected years if initial years are equal 28"
            ),
            pytest.param(
                (100, 100),
                [21, 17],
                id="check test with large numbers"
            )
        ]
    )
    def test_correct_expected_years(
            self,
            initial_years: tuple,
            expected_years: list) -> None:
        assert get_human_age(*initial_years) == expected_years

    @pytest.mark.parametrize(
        "initial_years, expected_error",
        [
            pytest.param(
                ("28", "28"),
                TypeError,
                id="should raise error if initial ages are of str type"
            ),
            pytest.param(
                ([28], [28]),
                TypeError,
                id="should raise error if initial ages are of list type"
            ),
        ]
    )
    def test_raise_correct_errors(
            self,
            initial_years: tuple,
            expected_error: Any) -> None:
        with pytest.raises(expected_error):
            get_human_age(initial_years)
