import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_years",
        [
            pytest.param(
                0, 0, [0, 0],
                id="return two zeroes when both ages are zero"
            ),
            pytest.param(
                -100, -100, [0, 0],
                id="return two zeroes when both ages are negative"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="first occurrence where numbers should differ"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="14 cat/dog years should convert into 0 human age."
            ),
            pytest.param(
                1256, 1256, [310, 248],
                id="should work properly with big numbers"
            ),
            pytest.param(
                25.2, 25.2, [2.0, 2.0],
                id="should work properly with float values"
            ),
        ]
    )
    def test_cat_and_d0g_age_to_human_age(
            self,
            cat_age: int,
            dog_age: int,
            human_years: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_years

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                "28", "28", TypeError,
                id="expected to raise TypeError when not int or float passed"
            )
        ]
    )
    def test_raising_correct_errors(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
