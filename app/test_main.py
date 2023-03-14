import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_age",
        [
            (-1, -1, [0, 0]),
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
        ]
    )
    def test_convert_ages_correctly(
            self,
            cat_age: int,
            dog_age: int,
            human_age: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age

    @pytest.mark.parametrize(
        "cat_age_non_integer,dog_age_non_integer",
        [
            ("non_integer", "non_integer"),
            ([2, 2], 4),
            (1, "non_integer")
        ]
    )
    def test_coin_is_int(
            self,
            cat_age_non_integer: int,
            dog_age_non_integer: int
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age_non_integer, dog_age_non_integer)
