from app.main import get_human_age
import pytest


class Testall:
    @pytest.mark.parametrize(
        "cat_years,dog_years,result",
        [
            (
                0,
                0,
                [0, 0]
            ),

            (
                14,
                14,
                [0, 0]
            ),
            (
                15,
                15,
                [1, 1]
            ),
            (
                23,
                23,
                [1, 1]
            ),
            (
                24,
                24,
                [2, 2]
            ),
            (
                27,
                27,
                [2, 2]
            ),
            (
                28,
                28,
                [3, 2]
            ),
            (
                100,
                100,
                [21, 17]
            ),
        ],
    )
    def test_convert_zero(
            self,
            cat_years: int,
            dog_years: int,
            result: list
    ) -> None:

        assert get_human_age(cat_years, dog_years) == result

    @pytest.mark.parametrize(
        "cat_years,dog_years,result",
        [
            (
                2,
                "53",
                [0, 0]
            )
        ])
    def test_type_data(self,
                       cat_years: int,
                       dog_years: int,
                       result: list) -> None:
        try:
            get_human_age(cat_years, dog_years)
        except TypeError:
            pytest.raises(TypeError)
