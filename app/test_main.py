import pytest
from typing import Any

from app.main import get_human_age


class TestHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
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
            (36, 47, [5, 6])
        ],
        ids=[
            "Should return [0, 0] when invalid input",
            "Should return [0, 0] when both values are zero",
            "Should return [0, 0] when both values under 15",
            "Should return [1, 1] when both values in range 15..23",
            "Should return [1, 1] when both values in range 15..23",
            "Should return [2, 2] when both values in range 24..27 ",
            "Should return [2, 2] when both values in range 24..27 ",
            "Should return [3, 2] when both values are 28",
            "Should return [21, 17] when both values are 100",
            "Should return [5, 6] when both values arre different"
        ]
    )
    def test_results_of_human_age(
        self,
        cat_age: int,
        dog_age: int,
        result: list[int, int]
    ) -> None:
        assert (
            get_human_age(cat_age, dog_age) == result
        ), "Should return list of two converted ages"

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_error",
        [
            ("1", "1", TypeError),
            ([2], {3}, TypeError),
            ((2, 3), {3: 1}, TypeError),
        ],
        ids=[
            "Raises TypeError when values are string",
            "Raises TypeError when values are mutable types",
            "Raises TypeError when values are types with values inside",
        ]
    )
    def test_raising_errors_correctly(
        self,
        cat_age: Any,
        dog_age: Any,
        expected_error: TypeError
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
