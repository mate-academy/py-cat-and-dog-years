import pytest
from app.main import get_human_age


class TestBasicCases:
    @pytest.mark.parametrize("cat, dog, expected", [
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ])
    def test_basic(self, cat: int, dog: int, expected: list) -> None:
        assert get_human_age(cat, dog) == expected


class TestEdgeCases:
    @pytest.mark.parametrize("cat, dog, expected", [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
    ])
    def test_boundaries(self, cat: int, dog: int, expected: list) -> None:
        assert get_human_age(cat, dog) == expected


class TestCatVsDog:
    @pytest.mark.parametrize("cat, dog, expected", [
        (28, 28, [3, 2]),
        (40, 40, [6, 5]),
    ])
    def test_differences(self, cat: int, dog: int, expected: list) -> None:
        assert get_human_age(cat, dog) == expected
