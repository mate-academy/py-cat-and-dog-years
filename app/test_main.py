import pytest
from app.main import get_human_age


class TestsCatAndDog:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17])
        ]
    )
    def test_should_calculate_correct_cat_and_dog_years(
            self, cat_age: int | str, dog_age: int | str, result: int | str
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result
