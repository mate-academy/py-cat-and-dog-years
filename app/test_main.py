import pytest
from app.main import get_human_age
from typing import List


class TestGetHumanAge:
    @pytest.mark.parametrize("cat_age, dog_age, expected", [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
    ])
    def test_get_human_age_valid_cases(
            self,
            cat_age: int,
            dog_age: int,
            expected: List[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize("cat_age, dog_age", [
        (-1, 5),
        (5, -10),
        (-20, -20),
    ])
    def test_negative_ages(self, cat_age: int, dog_age: int) -> None:
        result = get_human_age(cat_age, dog_age)
        assert all(age >= 0 for age in result)

    @pytest.mark.parametrize("cat_age, dog_age", [
        ("20", 20),
        (20, [20]),
        (None, 20),
        (20.5, 20),
    ])
    def test_invalid_types(self, cat_age: int, dog_age: int) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
