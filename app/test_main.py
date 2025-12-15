from app.main import get_human_age
import pytest


class TestGetHumanAge:
    """Test suite for get_human_age function"""

    def test_both_zero_age(self) -> None:
        """Test with both pets at age 0"""
        assert get_human_age(0, 0) == [0, 0]

    def test_both_under_first_threshold(self) -> None:
        """Test with both pets under 15 years"""
        assert get_human_age(14, 14) == [0, 0]
        assert get_human_age(10, 10) == [0, 0]
        assert get_human_age(1, 1) == [0, 0]

    def test_both_exactly_first_threshold(self) -> None:
        """Test with both pets exactly 15 years"""
        assert get_human_age(15, 15) == [1, 1]

    def test_both_in_second_range(self) -> None:
        """Test with both pets between 15 and 23 years"""
        assert get_human_age(16, 16) == [1, 1]
        assert get_human_age(20, 20) == [1, 1]
        assert get_human_age(23, 23) == [1, 1]

    def test_both_exactly_second_threshold(self) -> None:
        """Test with both pets exactly 24 years"""
        assert get_human_age(24, 24) == [2, 2]

    def test_both_at_27_years(self) -> None:
        """Test with both pets at 27 years"""
        assert get_human_age(27, 27) == [2, 2]

    def test_cat_and_dog_at_28_years(self) -> None:
        """Test at 28 years - cat gets 3, dog stays at 2"""
        assert get_human_age(28, 28) == [3, 2]

    def test_large_ages(self) -> None:
        """Test with large age value 100"""
        assert get_human_age(100, 100) == [21, 17]

    def test_cat_age_progression(self) -> None:
        """Test cat age conversion at various points"""
        # 0-14 cat years = 0 human years
        assert get_human_age(0, 0) == [0, 0]
        assert get_human_age(14, 0) == [0, 0]

        # 15-23 cat years = 1 human year
        assert get_human_age(15, 0) == [1, 0]
        assert get_human_age(23, 0) == [1, 0]

        # 24-27 cat years = 2 human years
        assert get_human_age(24, 0) == [2, 0]
        assert get_human_age(27, 0) == [2, 0]

        # 28-31 cat years = 3 human years (24 + 4)
        assert get_human_age(28, 0) == [3, 0]
        assert get_human_age(31, 0) == [3, 0]

        # 32-35 cat years = 4 human years (24 + 8)
        assert get_human_age(32, 0) == [4, 0]
        assert get_human_age(35, 0) == [4, 0]

        # 36-39 cat years = 5 human years (24 + 12)
        assert get_human_age(36, 0) == [5, 0]
        assert get_human_age(39, 0) == [5, 0]

    def test_dog_age_progression(self) -> None:
        """Test dog age conversion at various points"""
        # 0-14 dog years = 0 human years
        assert get_human_age(0, 0) == [0, 0]
        assert get_human_age(0, 14) == [0, 0]

        # 15-23 dog years = 1 human year
        assert get_human_age(0, 15) == [0, 1]
        assert get_human_age(0, 23) == [0, 1]

        # 24-28 dog years = 2 human years
        assert get_human_age(0, 24) == [0, 2]
        assert get_human_age(0, 28) == [0, 2]

        # 29-33 dog years = 3 human years (24 + 5)
        assert get_human_age(0, 29) == [0, 3]
        assert get_human_age(0, 33) == [0, 3]

        # 34-38 dog years = 4 human years (24 + 10)
        assert get_human_age(0, 34) == [0, 4]
        assert get_human_age(0, 38) == [0, 4]

        # 39-43 dog years = 5 human years (24 + 15)
        assert get_human_age(0, 39) == [0, 5]
        assert get_human_age(0, 43) == [0, 5]

    def test_different_ages_for_cat_and_dog(self) -> None:
        """Test with different ages for cat and dog"""
        assert get_human_age(15, 24) == [1, 2]
        assert get_human_age(24, 15) == [2, 1]
        assert get_human_age(28, 29) == [3, 3]
        assert get_human_age(36, 39) == [5, 5]

    def test_boundary_values_cat(self) -> None:
        """Test boundary values for cat age conversion"""
        assert get_human_age(14, 0) == [0, 0]  # Just before first threshold
        assert get_human_age(15, 0) == [1, 0]  # At first threshold
        assert get_human_age(23, 0) == [1, 0]  # Just before second threshold
        assert get_human_age(24, 0) == [2, 0]  # At second threshold
        assert get_human_age(27, 0) == [2, 0]  # Just before next increment
        assert get_human_age(28, 0) == [3, 0]  # At next increment
        assert get_human_age(31, 0) == [3, 0]  # Just before next increment
        assert get_human_age(32, 0) == [4, 0]  # At next increment

    def test_boundary_values_dog(self) -> None:
        """Test boundary values for dog age conversion"""
        assert get_human_age(0, 14) == [0, 0]  # Just before first threshold
        assert get_human_age(0, 15) == [0, 1]  # At first threshold
        assert get_human_age(0, 23) == [0, 1]  # Just before second threshold
        assert get_human_age(0, 24) == [0, 2]  # At second threshold
        assert get_human_age(0, 28) == [0, 2]  # Just before next increment
        assert get_human_age(0, 29) == [0, 3]  # At next increment
        assert get_human_age(0, 33) == [0, 3]  # Just before next increment
        assert get_human_age(0, 34) == [0, 4]  # At next increment

    def test_return_type(self) -> None:
        """Test that function returns a list"""
        result = get_human_age(15, 15)
        assert isinstance(result, list)
        assert len(result) == 2

    def test_return_values_are_integers(self) -> None:
        """Test that returned values are integers"""
        result = get_human_age(15, 15)
        assert isinstance(result[0], int)
        assert isinstance(result[1], int)

    def test_remainder_discarded_cat(self) -> None:
        """Test that remainders are properly discarded for cats"""
        # 25 = 24 + 1, so 2 + (1 // 4) = 2
        assert get_human_age(25, 0) == [2, 0]
        # 26 = 24 + 2, so 2 + (2 // 4) = 2
        assert get_human_age(26, 0) == [2, 0]
        # 27 = 24 + 3, so 2 + (3 // 4) = 2
        assert get_human_age(27, 0) == [2, 0]

    def test_remainder_discarded_dog(self) -> None:
        """Test that remainders are properly discarded for dogs"""
        # 25 = 24 + 1, so 2 + (1 // 5) = 2
        assert get_human_age(0, 25) == [0, 2]
        # 26 = 24 + 2, so 2 + (2 // 5) = 2
        assert get_human_age(0, 26) == [0, 2]
        # 28 = 24 + 4, so 2 + (4 // 5) = 2
        assert get_human_age(0, 28) == [0, 2]

    def test_edge_case_first_year(self) -> None:
        """Test edge cases for ages under 15"""
        assert get_human_age(1, 1) == [0, 0]
        assert get_human_age(7, 7) == [0, 0]
        assert get_human_age(13, 13) == [0, 0]
        assert get_human_age(14, 14) == [0, 0]

    def test_mixed_ranges(self) -> None:
        """Test with pets in different age ranges"""
        assert get_human_age(10, 20) == [0, 1]
        assert get_human_age(20, 10) == [1, 0]
        assert get_human_age(30, 35) == [3, 4]
        assert get_human_age(50, 60) == [8, 9]

    def test_very_large_ages(self) -> None:
        """Test with very large age values"""
        # Cat: 200 = 24 + 176, so 2 + (176 // 4) = 2 + 44 = 46
        # Dog: 200 = 24 + 176, so 2 + (176 // 5) = 2 + 35 = 37
        assert get_human_age(200, 200) == [46, 37]

    def test_specific_example_cases(self) -> None:
        """Test all specific examples from the problem statement"""
        assert get_human_age(0, 0) == [0, 0]
        assert get_human_age(14, 14) == [0, 0]
        assert get_human_age(15, 15) == [1, 1]
        assert get_human_age(23, 23) == [1, 1]
        assert get_human_age(24, 24) == [2, 2]
        assert get_human_age(27, 27) == [2, 2]
        assert get_human_age(28, 28) == [3, 2]
        assert get_human_age(100, 100) == [21, 17]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
