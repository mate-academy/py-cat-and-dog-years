import pytest
from app.main import get_human_age


class TestGetHumanAge:

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 14, [1, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
            (1000, 1000, [246, 197]),
        ]
    )
    def test_get_human_age(self, cat_age: int, dog_age: int, expected: list) -> None:
        result = get_human_age(cat_age, dog_age)
        assert result == expected

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            (-5, -5),
            (0,0),
            (None, None),
            ("cat","dog")
        ]
    )
    def test_invalid_input(self, cat_age: int, dog_age: int) -> None:
        with pytest.raises((ValueError, TypeError)):
            get_human_age(cat_age, dog_age)