from app.main import get_human_age

import pytest


class TestCatDogYears:
    @pytest.mark.parametrize(
        "cat_years,dog_years,expected_years",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17])
        ]
    )
    def test_receive_correct_value_type(
            self,
            cat_years: int,
            dog_years: int,
            expected_years: int
    ) -> None:
        assert get_human_age(cat_years, dog_years) == expected_years

    @pytest.mark.parametrize(
        "cat_years,dog_years",
        [
            (-1, 0),
            (14, -1),
        ]
    )
    def test_negative_values_errors(
            self,
            cat_years: int,
            dog_years: int,
    ) -> None:
        with pytest.raises(AssertionError):
            assert cat_years > 0
            assert dog_years > 0

    @pytest.mark.parametrize(
        "cat_years,dog_years,exception_error",
        [
            pytest.param(
                "t", 0, TypeError,
                id="should rise error when wrong type"
            ),
        ]
    )
    def test_values_errors(
            self,
            cat_years: int,
            dog_years: int,
            exception_error: str
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_years, dog_years)
