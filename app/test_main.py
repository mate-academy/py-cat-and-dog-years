import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
            (5, -1, [0, 0]),
            (1000, 2000, [246, 397]),
        ]
    )
    def test_get_age_correct(self,
                             cat_age: int,
                             dog_age: int,
                             expected: list) -> None:
        assert get_human_age(cat_age, dog_age) == expected, (
            f"Expected {expected} when cat's age "
            f"is {cat_age} and dog's age is {dog_age}, "
            f"but got {get_human_age(cat_age, dog_age)} instead."
        )

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ("17", 6),
            (None, 17.8),
            ([14], 3)
        ]
    )
    def test_get_age_incorrect(self, cat_age: int, dog_age: int) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
