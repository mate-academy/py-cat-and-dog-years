from typing import List, Any
import pytest
from app.main import get_human_age


class TestGetHumanAge:
    # Basic test cases
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (-1, 0, [0, 0]),
            (0, -1, [0, 0]),
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
        ],
        ids=[
            "Negative cat age",
            "Negative dog age",
            "Zero ages",
            "Both animals are in young age",
            "Both animals are in young age, just above the boundary",
            "Boundary ages for young",
            "Age just above the boundary",
            "Boundary ages for adult",
            "Age just above the boundary",
            "Boundary ages for senior cat",
        ]
    )
    def test_basic_cases(
            self,
            cat_age: Any,
            dog_age: Any,
            expected: List[Any]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ("-1", 10),
            (10, "1"),
            ("0", 10),
            (10, "0"),
            ("1000", "1000"),
            ("10", 10),
            (10, "10"),
            ([10], 10),
            (10, [10]),
        ],
        ids=[
            "Negative cat age",
            "Negative dog age",
            "Zero cat age",
            "Zero dog age",
            "Very large ages",
            "String cat age",
            "String dog age",
            "List cat age",
            "List dog age",
        ]
    )
    def test_error_will_be_raised(
        self,
        cat_age: Any,
        dog_age: Any
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
