import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (0, 0, [0, 0]),
            (10, 14, [0, 0]),

            (15, 15, [1, 1]),

            (20, 23, [1, 1]),

            (24, 25, [2, 2]),

            (28, 30, [3, 3]),
            (40, 40, [6, 5]),

            (23, 24, [1, 2]),
            (24, 29, [2, 3]),
        ],
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected
