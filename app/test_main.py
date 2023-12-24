import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_years",
        [
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (29, 29, [3, 3]),
            (50, 50, [8, 7])
        ]

    )
    def test_year_change(
        self,
        cat_age: int,
        dog_age: int,
        human_years: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_years

    @pytest.mark.parametrize(
        "cat_age,dog_age,human_years",
        [
            (-10, -10, [0, 0]),
            (0, 0, [0, 0])
        ]
    )
    def test_out_of_range_age(
        self,
        cat_age: int,
        dog_age: int,
        human_years: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_years
