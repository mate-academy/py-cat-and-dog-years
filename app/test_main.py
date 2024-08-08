import pytest

from app.main import get_human_age


class TestGetAge:
    @pytest.mark.parametrize(
        "dog_age", "cat_age", "excepted_age",
        [
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
    def test_correctly_age(
            self,
            dog_age: int,
            cat_age: int,
            excepted_age: list
    ) -> None:
        assert get_human_age(dog_age, cat_age) == excepted_age
