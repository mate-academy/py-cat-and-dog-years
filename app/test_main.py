from app.main import get_human_age
import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_years, dog_years, expected_years_list",
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
    def test_get_correctly_human_age(
        self,
        cat_years: int,
        dog_years: int,
        expected_years_list: list[int]
    ) -> None:
        assert get_human_age(cat_years, dog_years) == expected_years_list
