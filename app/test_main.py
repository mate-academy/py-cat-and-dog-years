from app.main import get_human_age
import pytest


class TestDogCatAge:
    @pytest.mark.parametrize(
        "age_cat,age_dog,result",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 29, [3, 3]),
            (100, 100, [21, 17])
        ]
    )
    def test_cat_dog(self, age_dog: int, age_cat: int, result: list) -> None:

        assert get_human_age(age_cat, age_dog) == result
