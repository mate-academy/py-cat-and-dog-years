from app.main import get_human_age

import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize("cat_age, dog_age, expected", [
        (14, 0, [0, 0]),
        (15, 0, [1, 0]),
        (23, 0, [1, 0]),
        (24, 0, [2, 0]),
        (29, 0, [3, 0]),
        (56, 0, [10, 0]),
        (99, 0, [20, 0]),

        (0, 14, [0, 0]),
        (0, 15, [0, 1]),
        (0, 23, [0, 1]),
        (0, 24, [0, 2]),
        (0, 29, [0, 3]),
        (0, 56, [0, 8]),
        (0, 99, [0, 17]),

        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (29, 29, [3, 3]),
        (56, 56, [10, 8]),
        (99, 99, [20, 17]),
    ])
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected
