import pytest

from app.main import get_human_age


class TestConvertAnimalAgeToHuman:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_ages",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
        ],
    )
    def test_converting_age(
            self,
            cat_age: int,
            dog_age: int,
            expected_ages: list
    ) -> None:

        assert get_human_age(cat_age, dog_age) == expected_ages
