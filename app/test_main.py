import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result_convert_to_human_age",
        [
            (14, 14, [0, 0]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (28, 29, [3, 3]),
            (100, 100, [21, 17])
        ]
    )
    def test_calculate_human_age(
            self,
            cat_age: int,
            dog_age: int,
            result_convert_to_human_age: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result_convert_to_human_age
