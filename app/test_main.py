import pytest

from app.main import get_human_age


class TestHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
        [
            (0, 0, [0, 0]),
            (1, 2, [0, 0]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17])
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected: list
    ) -> None:
        assert (get_human_age(cat_age, dog_age) == expected),\
            (f"Expected {expected} when cat's age "
             f"is {cat_age} and dog's age is {dog_age}")
