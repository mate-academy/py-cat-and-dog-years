import pytest

from app.main import get_human_age


class TestConvertAge:
    @pytest.mark.parametrize(
        "cat_years,dog_years,list_of_human_ages",
        [
            pytest.param(0, 0, [0, 0],),
            pytest.param(15, 15, [1, 1]),
            pytest.param(24, 24, [2, 2]),
            pytest.param(28, 28, [3, 2]),
            pytest.param(100, 100, [21, 17])
        ]
    )
    def test_convert_to_human_age(
            self,
            cat_years: int,
            dog_years: int,
            list_of_human_ages: list
    ) -> None:
        assert get_human_age(cat_years, dog_years) == list_of_human_ages
