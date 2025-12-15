import pytest
from typing import List, Any
from .main import get_human_age


class TestGetHumanAge:
    """Test suite for get_human_age function"""

    @pytest.mark.parametrize("cat_age, dog_age, expected", [
        # Both zero age
        (0, 0, [0, 0]),

        # Both under first threshold (< 15)
        (1, 1, [0, 0]),
        (7, 7, [0, 0]),
        (10, 10, [0, 0]),
        (13, 13, [0, 0]),
        (14, 14, [0, 0]),

        # Both exactly at first threshold (15)
        (15, 15, [1, 1]),

        # Both in second range (15-23)
        (16, 16, [1, 1]),
        (20, 20, [1, 1]),
        (23, 23, [1, 1]),

        # Both exactly at second threshold (24)
        (24, 24, [2, 2]),

        # Both at 27 years
        (27, 27, [2, 2]),

        # Cat and dog at 28 years (cat gets 3, dog stays at 2)
        (28, 28, [3, 2]),

        # Large ages
        (100, 100, [21, 17]),
        (200, 200, [46, 37]),
    ])
    def test_both_same_age(self, cat_age, dog_age, expected):
        """Test with both pets at the same age"""
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize("cat_age, expected_cat_human_age", [
        # 0-14 cat years = 0 human years
        (0, 0),
        (14, 0),

        # 15-23 cat years = 1 human year
        (15, 1),
        (23, 1),

        # 24-27 cat years = 2 human years
        (24, 2),
        (27, 2),

        # 28-31 cat years = 3 human years
        (28, 3),
        (31, 3),

        # 32-35 cat years = 4 human years
        (32, 4),
        (35, 4),

        # 36-39 cat years = 5 human years
        (36, 5),
        (39, 5),

        # Larger ages
        (50, 8),
        (100, 21),
    ])
    def test_cat_age_progression(self, cat_age, expected_cat_human_age):
        """Test cat age conversion at various points"""
        assert get_human_age(cat_age, 0)[0] == expected_cat_human_age

    @pytest.mark.parametrize("dog_age, expected_dog_human_age", [
        # 0-14 dog years = 0 human years
        (0, 0),
        (14, 0),

        # 15-23 dog years = 1 human year
        (15, 1),
        (23, 1),

        # 24-28 dog years = 2 human years
        (24, 2),
        (28, 2),

        # 29-33 dog years = 3 human years
        (29, 3),
        (33, 3),

        # 34-38 dog years = 4 human years
        (34, 4),
        (38, 4),

        # 39-43 dog years = 5 human years
        (39, 5),
        (43, 5),

        # Larger ages
        (60, 9),
        (100, 17),
    ])
    def test_dog_age_progression(self, dog_age, expected_dog_human_age):
        """Test dog age conversion at various points"""
        assert get_human_age(0, dog_age)[1] == expected_dog_human_age

    @pytest.mark.parametrize("cat_age, dog_age, expected", [
        # Different ages for cat and dog
        (15, 24, [1, 2]),
        (24, 15, [2, 1]),
        (28, 29, [3, 3]),
        (36, 39, [5, 5]),
        (10, 20, [0, 1]),
        (20, 10, [1, 0]),
        (30, 35, [3, 4]),
    ])
    def test_different_ages(self, cat_age, dog_age, expected):
        """Test with different ages for cat and dog"""
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize("cat_age, expected_cat_human_age", [
        # Boundary values for cat
        (14, 0),  # Just before first threshold
        (15, 1),  # At first threshold
        (23, 1),  # Just before second threshold
        (24, 2),  # At second threshold
        (27, 2),  # Just before next increment
        (28, 3),  # At next increment
        (31, 3),  # Just before next increment
        (32, 4),  # At next increment
    ])
    def test_cat_boundary_values(self, cat_age, expected_cat_human_age):
        """Test boundary values for cat age conversion"""
        assert get_human_age(cat_age, 0)[0] == expected_cat_human_age

    @pytest.mark.parametrize("dog_age, expected_dog_human_age", [
        # Boundary values for dog
        (14, 0),  # Just before first threshold
        (15, 1),  # At first threshold
        (23, 1),  # Just before second threshold
        (24, 2),  # At second threshold
        (28, 2),  # Just before next increment
        (29, 3),  # At next increment
        (33, 3),  # Just before next increment
        (34, 4),  # At next increment
    ])
    def test_dog_boundary_values(self, dog_age, expected_dog_human_age):
        """Test boundary values for dog age conversion"""
        assert get_human_age(0, dog_age)[1] == expected_dog_human_age

    @pytest.mark.parametrize("cat_age, expected_cat_human_age", [
        # Test remainder discarding for cats (every 4 years after 24)
        (25, 2),  # 24 + 1, so 2 + (1 // 4) = 2
        (26, 2),  # 24 + 2, so 2 + (2 // 4) = 2
        (27, 2),  # 24 + 3, so 2 + (3 // 4) = 2
    ])
    def test_cat_remainder_discarded(self, cat_age, expected_cat_human_age):
        """Test that remainders are properly discarded for cats"""
        assert get_human_age(cat_age, 0)[0] == expected_cat_human_age

    @pytest.mark.parametrize("dog_age, expected_dog_human_age", [
        # Test remainder discarding for dogs (every 5 years after 24)
        (25, 2),  # 24 + 1, so 2 + (1 // 5) = 2
        (26, 2),  # 24 + 2, so 2 + (2 // 5) = 2
        (28, 2),  # 24 + 4, so 2 + (4 // 5) = 2
    ])
    def test_dog_remainder_discarded(self, dog_age, expected_dog_human_age):
        """Test that remainders are properly discarded for dogs"""
        assert get_human_age(0, dog_age)[1] == expected_dog_human_age

    def test_return_type(self):
        """Test that function returns a list"""
        result = get_human_age(15, 15)
        assert isinstance(result, list)
        assert len(result) == 2

    def test_return_values_are_integers(self):
        """Test that returned values are integers"""
        result = get_human_age(15, 15)
        assert isinstance(result[0], int)
        assert isinstance(result[1], int)

    @pytest.mark.parametrize("cat_age, dog_age, expected", [
        # All specific examples from problem statement
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ])
    def test_specific_examples(self, cat_age, dog_age, expected):
        """Test all specific examples from the problem statement"""
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize("cat_age, dog_age", [
        (-1, 0),
        (0, -1),
        (-5, -5),
        (-10, 10),
        (10, -10),
    ])
    def test_negative_ages(self, cat_age, dog_age):
        """Test that function handles negative ages appropriately"""
        result = get_human_age(cat_age, dog_age)
        assert isinstance(result, list)
        assert len(result) == 2

    @pytest.mark.parametrize("cat_age, dog_age", [
        ("15", 15),
        (15, "15"),
        ("cat", "dog"),
        (15.5, 15),
        (15, 15.5),
        (None, 15),
        (15, None),
        ([15], 15),
        (15, [15]),
    ])
    def test_invalid_data_types(self, cat_age, dog_age):
        """Test that function raises TypeError for invalid data types"""
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
