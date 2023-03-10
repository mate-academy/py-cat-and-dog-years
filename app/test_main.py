import pytest

from app.main import get_human_age


class TestConvertYears:
    @pytest.mark.parametrize(
        "cat_years,dog_years,human_years",
        [
            pytest.param(
                14,
                14,
                [0, 0],
                id="should convert into 0 human age"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="should convert into 1 human age"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="should convert into 1 human age"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="should convert into 2 human age"
            ),
            pytest.param(
                27,
                28,
                [2, 2],
                id="should convert into 2 human age"
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="should convert into 3 human age"
            )
        ]
    )
    def test_convert_to_human_age(
            self,
            cat_years: int,
            dog_years: int,
            human_years: int
    ) -> None:
        assert get_human_age(cat_years, dog_years) == human_years
