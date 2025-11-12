from typing import Any

import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            (-1, -1, [0, 0]),
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17])
        ],
        ids=[
            "[0, 0] if invalid negative input",
            "[0, 0] zero age",
            "[0, 0] for range < 15",
            "[0, 0] boundary case 15",
            "[1, 1] if age in range 15...23",
            "[2, 2] boundary case 24",
            "[2, 2] if age in range 24...27",
            "[3, 2] boundary diff for 28",
            "[21, 17] large numbers"
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result

    @pytest.mark.parametrize(
        "cat_age,dog_age,error",
        [
            (1, "1", TypeError),
            ([1], {1: 1}, TypeError),
            ((1, 2), True, TypeError),
        ]
    )
    def test_raising_errors(
            self,
            cat_age: Any,
            dog_age: Any,
            error: TypeError
    ) -> None:
        with pytest.raises(error):
            get_human_age(cat_age, dog_age)
