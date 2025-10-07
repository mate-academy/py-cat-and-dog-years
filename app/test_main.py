import pytest
from app.main import get_human_age


class TestGetHumanAge:
    """Test suite for get_human_age function."""

    def test_zero_age(self):
        """Test with zero age for both cat and dog."""
        assert get_human_age(0, 0) == [0, 0]

    def test_below_first_threshold(self):
        """Test ages below the first threshold (15 years)."""
        assert get_human_age(14, 14) == [0, 0]
        assert get_human_age(1, 1) == [0, 0]
        assert get_human_age(10, 10) == [0, 0]

    def test_exactly_first_threshold(self):
        """Test exactly at the first threshold (15 years = 1 human year)."""
        assert get_human_age(15, 15) == [1, 1]

    def test_between_first_and_second_threshold(self):
        """Test ages between first threshold (15) and second threshold (24)."""
        assert get_human_age(16, 16) == [1, 1]
        assert get_human_age(20, 20) == [1, 1]
        assert get_human_age(23, 23) == [1, 1]

    def test_exactly_second_threshold(self):
        """Test exactly at the second threshold (15+9=24 years = 2 human years)."""
        assert get_human_age(24, 24) == [2, 2]

    def test_after_second_threshold(self):
        """Test ages after the second threshold where cat and dog diverge."""
        # Cat: every 4 years, Dog: every 5 years
        assert get_human_age(27, 27) == [2, 2]
        assert get_human_age(28, 28) == [3, 2]  # Cat gets 3rd year at 28, dog still at 2
        assert get_human_age(29, 29) == [3, 3]  # Dog gets 3rd year at 29
        assert get_human_age(32, 32) == [4, 3]  # Cat: 24+8=32 -> 4 years, Dog: 24+8=32 -> 3 years
        assert get_human_age(36, 36) == [5, 4]  # Cat: 24+12=36 -> 5 years, Dog: 24+12=36 -> 4 years

    def test_large_ages(self):
        """Test with large ages."""
        assert get_human_age(100, 100) == [21, 17]

    def test_cat_older_than_dog(self):
        """Test when cat age is different from dog age (cat older)."""
        assert get_human_age(50, 30) == [8, 3]
        assert get_human_age(28, 15) == [3, 1]

    def test_dog_older_than_cat(self):
        """Test when dog age is different from cat age (dog older)."""
        assert get_human_age(15, 50) == [1, 7]
        assert get_human_age(24, 40) == [2, 5]

    def test_boundary_cat_every_4_years(self):
        """Test cat age boundaries for the 'every 4 years' rule."""
        # After 24, every 4 cat years = 1 human year
        assert get_human_age(24, 0) == [2, 0]  # Base: 2 human years
        assert get_human_age(27, 0) == [2, 0]  # 24 + 3 = 27 -> still 2
        assert get_human_age(28, 0) == [3, 0]  # 24 + 4 = 28 -> 3
        assert get_human_age(31, 0) == [3, 0]  # 24 + 7 = 31 -> still 3
        assert get_human_age(32, 0) == [4, 0]  # 24 + 8 = 32 -> 4
        assert get_human_age(40, 0) == [6, 0]  # 24 + 16 = 40 -> 6

    def test_boundary_dog_every_5_years(self):
        """Test dog age boundaries for the 'every 5 years' rule."""
        # After 24, every 5 dog years = 1 human year
        assert get_human_age(0, 24) == [0, 2]  # Base: 2 human years
        assert get_human_age(0, 28) == [0, 2]  # 24 + 4 = 28 -> still 2
        assert get_human_age(0, 29) == [0, 3]  # 24 + 5 = 29 -> 3
        assert get_human_age(0, 33) == [0, 3]  # 24 + 9 = 33 -> still 3
        assert get_human_age(0, 34) == [0, 4]  # 24 + 10 = 34 -> 4
        assert get_human_age(0, 50) == [0, 7]  # 24 + 26 = 50 -> 7

    def test_exact_thresholds_independently(self):
        """Test exact threshold values for cat and dog independently."""
        # Cat thresholds: 15, 24, 28, 32, 36...
        assert get_human_age(15, 0) == [1, 0]
        assert get_human_age(24, 0) == [2, 0]
        assert get_human_age(28, 0) == [3, 0]

        # Dog thresholds: 15, 24, 29, 34, 39...
        assert get_human_age(0, 15) == [0, 1]
        assert get_human_age(0, 24) == [0, 2]
        assert get_human_age(0, 29) == [0, 3]
        assert get_human_age(0, 34) == [0, 4]

    def test_asymmetric_ages(self):
        """Test various asymmetric age combinations."""
        assert get_human_age(100, 15) == [21, 1]
        assert get_human_age(15, 100) == [1, 17]
        assert get_human_age(50, 60) == [8, 9]
