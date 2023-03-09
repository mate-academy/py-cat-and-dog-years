import pytest

from app.main import get_human_age


class TestConvertYears:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_age",
        [
            pytest.param(
                0, 0,
                [0, 0],
                id="should return zeroes when integers are zeroes"

            ),
            pytest.param(
                14, 14,
                [0, 0],
                id="should return zeroes when integers less first year"
            ),
            pytest.param(
                15, 15,
                [1, 1],
                id="should return one when integers less second year"
            ),
            pytest.param(
                27, 27,
                [2, 2],
                id="should return one when integers less third year"
            ),
            pytest.param(
                28, 28,
                [3, 2],
                id="should return validates years for each animal"
            ),
            pytest.param(
                100, 100,
                [21, 17],
                id="should check huge numbers"
            )
        ]
    )
    def test_convert_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            human_age: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age
