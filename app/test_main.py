import pytest
from app.main import get_human_age


class TestPyCatAndDogYears:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result_list",
        [
            (
                14,
                14,
                [0, 0]
            ),
            (
                15,
                15,
                [1, 1]
            ),
            (
                28,
                28,
                [3, 2]
            ),
            (
                0,
                0,
                [0, 0]
            ),
        ]
    )
    def test_py_cat_and_dog_years(self, cat_age: int, dog_age: int, result_list: list) -> None:
        assert get_human_age(cat_age, dog_age) == result_list
