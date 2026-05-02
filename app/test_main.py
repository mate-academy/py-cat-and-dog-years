import unittest
from app.main import get_human_age


class TestGetHumanAge(unittest.TestCase):

    def test_zero_age(self) -> None:
        assert get_human_age(0, 0) == [0, 0]

    def test_cat_and_dog_below_first_threshold(self) -> None:
        assert get_human_age(14, 14) == [0, 0]

    def test_exactly_15_years(self) -> None:
        assert get_human_age(15, 15) == [1, 1]

    def test_between_15_and_24_years(self) -> None:
        assert get_human_age(23, 23) == [1, 1]

    def test_exactly_24_years(self) -> None:
        assert get_human_age(24, 24) == [2, 2]

    def test_between_24_and_28_years(self) -> None:
        assert get_human_age(27, 27) == [2, 2]

    def test_exactly_28_years(self) -> None:
        assert get_human_age(28, 28) == [3, 2]

    def test_large_values(self) -> None:
        assert get_human_age(100, 100) == [21, 17]
