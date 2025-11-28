import pytest
from app.main import get_human_age


class TestGetHumanAge:

    age_cases_data = [
        # (cat_age, dog_age, expected_result)
        # edge cases data
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        # conversion boundaries data
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        # large values data
        (100, 100, [21, 17]),
        (50, 50, [8, 7]),
        (200, 200, [46, 37]),
        # additional boundaries data
        (16, 16, [1, 1]),
        (29, 29, [3, 3]),
        (32, 32, [4, 3]),
        (36, 36, [5, 4]),
    ]

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
        age_cases_data
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected: list) -> None:
        """Test get_human_age function with various inputs"""
        result = get_human_age(cat_age, dog_age)
        assert result == expected, (f"Failed for "
                                    f"cat_age={cat_age}, "
                                    f"dog_age={dog_age}. "
                                    f"Expected {expected}, got {result}")
