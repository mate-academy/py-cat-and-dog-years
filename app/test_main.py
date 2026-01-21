from typing import List
import pytest
from app.main import get_human_age


class TestRightValue:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_list",
        [
            pytest.param(
                0, 0, [0, 0],
                id="Both cat and dog ages are zero"
            ),
            pytest.param(
                10, 10, [0, 0],
                id="Both cat and dog ages are below 15 years"
            ),
            pytest.param(
                15, 15, [1, 1],
                id=("Both cat and dog ages are minimum (15 years) "
                    "for the first human year")
            ),
            pytest.param(
                23, 23, [1, 1],
                id="Both cat and dog ages are equal for the second human year"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="Cat and dog ages are unequal for the third human year"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="Cat and dog years increasing unproportional"
            )
        ]
    )
    def test_check_value_result(
            self,
            cat_age: int,
            dog_age: int,
            expected_list: List[int]) -> None:

        assert get_human_age(cat_age, dog_age) == expected_list

    def test_check_value_type(self) -> None:
        cat_age = 2
        dog_age = 10

        if not isinstance(get_human_age(cat_age, dog_age)[0], int):
            raise TypeError("cat_age must be an integer")

        if not isinstance(get_human_age(cat_age, dog_age)[1], int):
            raise TypeError("dog_age must be an integer")
