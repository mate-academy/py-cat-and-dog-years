import pytest
from app.main import get_human_age


class TestYearsCatDog:
    @pytest.mark.parametrize("cat_age, dog_age, expected", [
        (0, 0, [0, 0]),
        (-5, -5, [0, 0]),
        (15, 15, [1, 1]),
        (28, 28, [3, 2]),
        (32, 32, [4, 3]),
        (36, 36, [5, 4]),
        (40, 40, [6, 5]),
        (44, 44, [7, 6]),
        (100, 100, [21, 17]),
    ])
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected: list,
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    def test_invalid__type(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("cat_age", "dog_age")
