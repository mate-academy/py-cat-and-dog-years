import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_years,dog_years,expected",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
            ("str", "str", TypeError),
            (-1, -1, [0, 0])
        ]
    )
    def test_for_dog_and_cat_years(
            self,
            cat_years: int,
            dog_years: int,
            expected: list
    ) -> None:
        if isinstance(expected, type) and issubclass(expected, Exception):

            with pytest.raises(expected):
                get_human_age(cat_years, dog_years)
        else:
            assert get_human_age(cat_years, dog_years) == expected
