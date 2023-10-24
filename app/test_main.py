import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @staticmethod
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (-1, -2, [0, 0]),
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
    def test_pets_age_convert_to_human(
            cat_age: int,
            dog_age: int,
            expected: list
    ) -> None:
        assert (get_human_age(cat_age, dog_age)) == expected

    @staticmethod
    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ([1], 0),
            (0, [1]),
            (0, {1}),
            ({0}, 1),
            (0, "1"),
            ("1", 0),
        ]
    )
    def test_pets_age_invalid_type(cat_age: int, dog_age: int) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
