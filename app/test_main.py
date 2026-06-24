import pytest
from app.main import get_human_age


class TestBasicCases:
    @pytest.mark.parametrize("cat, dog, expected", [
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (100, 100, [21, 17]),
    ])
    def test_basic(self, cat: int, dog: int, expected: list) -> None:
        assert get_human_age(cat, dog) == expected


class TestEdgeCases:
    @pytest.mark.parametrize("cat, dog, expected", [
        (14, 14, [0, 0]),
        (23, 23, [1, 1]),
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


class TestInvalidInput:
    @pytest.mark.parametrize("cat, dog", [
        (-1, 10),
        (10, -1),
        (-5, -5),
        (1000, 10),
        (10, 1000),
    ])
    def test_negative_and_large(self, cat: int, dog: int) -> None:
        with pytest.raises(ValueError):
            get_human_age(cat, dog)
    @pytest.mark.parametrize("cat, dog", [
        ("15", 10),
        (10, "15"),
        (15.5, 10),
        (10, 15.5),
    ])
    def test_wrong_types(self, cat, dog) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat, dog)

class TestMixedRanges:
    @pytest.mark.parametrize("cat, dog, expected", [
        (10, 25, [0, 2]),
        (25, 10, [2, 0]),
        (30, 20, [3, 1]),
    ])
    def test_independent_calculation(self, cat, dog, expected):
        assert get_human_age(cat, dog) == expected
