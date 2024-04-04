import pytest
from typing import List
from app.main import get_human_age


class TestGetHumanAge:
    # Basic test cases
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
        ]
    )
    def test_basic_cases(
            self,
            cat_age: int,
            dog_age: int,
            expected: List[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected


class TestEdgeCases:
    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ("-1", 10),  # Negative cat age
            (10, "1"),  # Negative dog age
            ("0", 10),   # Zero cat age
            (10, "0"),   # Zero dog age
            ("1000", "1000"),  # Very large ages
            ("10", 10),  # String cat age
            (10, "10"),  # String dog age
            ([10], 10),  # List cat age
            (10, [10]),  # List dog age
        ]
    )
    def test_edge_cases(self, cat_age: int, dog_age: int) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
