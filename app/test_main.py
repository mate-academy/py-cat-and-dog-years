import pytest
from app.main import get_human_age


class TestGetHumanAgePositiveScenario:

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
        # negative values
        (-1, 0, [0, 0]),
        (0, -1, [0, 0]),
        (-5, -5, [0, 0]),
        (-100, 10, [0, 0]),
        (10, -100, [0, 0])
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


class TestGetHumanAgeNegativeScenario:

    def test_incorrect_data_types(self) -> None:
        """Test that incorrect data types raise TypeError"""
        # Test with strings
        with pytest.raises(TypeError):
            get_human_age("15", 15)

        with pytest.raises(TypeError):
            get_human_age("cat", "dog")

        # Test with None
        with pytest.raises(TypeError):
            get_human_age(None, 15)

        with pytest.raises(TypeError):
            get_human_age(15, None)

        # Test with lists
        with pytest.raises(TypeError):
            get_human_age([15], 15)
