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
                14, 14, [0, 0],
                id="14 cat/dog years should convert into 0 human age."
            ),
            pytest.param(
                15, 15, [1, 1],
                id="15 cat/dog years should convert into 1, 1 human age."
            ),
            pytest.param(
                23, 23, [1, 1],
                id="23 cat/dog years should convert into 1, 1 human age."
            ),
            pytest.param(
                24, 24, [2, 2],
                id="24 cat/dog years should convert into 2, 2 human age."
            ),
            pytest.param(
                25.2, 25.2, [2.0, 2.0],
                id="should work properly with float values"
            ),
            pytest.param(
                27, 27, [2, 2],
                id="27 cat/dog years should convert into 2, 2 human age."
            ),
            pytest.param(
                28, 28, [3, 2],
                id="first occurrence where numbers should differ"
            ),

            pytest.param(
                1256, 1256, [310, 248],
                id="should work properly with big numbers"
            ),

        ]
    )
    def test_cat_and_dog_age_to_human_age(
            self,
            cat_age: int,
            dog_age: int,
            human_years: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_years


def test_correct_input() -> None:
    with pytest.raises(TypeError):
        get_human_age("28", "28")
