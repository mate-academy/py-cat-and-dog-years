from app.main import get_human_age
import pytest


class TestGetHumanAge:
    """Test cases for get_human_age function."""

    @pytest.mark.parametrize("cat_age, dog_age, expected", [
        # Official examples
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        # Boundary transitions
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        # Edge cases
        (-1, -1, [0, 0]),
        (1000, 1000, [246, 197]),
        # Different combinations
        (24, 15, [2, 1]),
        (28, 24, [3, 2]),
        (100, 50, [21, 7]),
    ])
    def test_valid_inputs(
        self, cat_age: int, dog_age: int, expected: list
    ) -> None:
        """Test function with valid inputs."""
        assert get_human_age(cat_age, dog_age) == expected

    def test_result_structure(self) -> None:
        """Test result always has correct structure."""
        result = get_human_age(15, 15)
        assert isinstance(result, list)
        assert len(result) == 2
        assert all(isinstance(x, int) for x in result)
        assert all(x >= 0 for x in result)

    @pytest.mark.parametrize("cat_age, dog_age", [
        ("15", 15),
        (15, "15"),
        (None, 15),
        ([15], 15),
    ])
    def test_invalid_input_types_that_actually_raise_errors(
        self, cat_age: int, dog_age: int
    ) -> None:
        """Test function raises error with truly invalid input types."""
        with pytest.raises((TypeError, ValueError)):
            get_human_age(cat_age, dog_age)
