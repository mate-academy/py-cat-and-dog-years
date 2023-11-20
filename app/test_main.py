import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_age",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
            (5968, 5240, [1488, 1045]),
            (-100, 0, [0, 0]),
            (0, -100, [0, 0]),
            (-100000, -100000, [0, 0]),
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            human_age: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age
