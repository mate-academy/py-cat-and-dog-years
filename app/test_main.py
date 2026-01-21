from typing import Type

import pytest

from app.main import get_human_age


class TestCheckAgeCatAndDogClass:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_age",
        [
            pytest.param(
                6,
                15,
                [0, 1],
                id="zero if cat_age is less then 15"
            ),
            pytest.param(
                17,
                8,
                [1, 0],
                id="zero if dog_age is less then 15"
            ),
            pytest.param(
                5,
                4,
                [0, 0],
                id="zero if cat_age and dog_age is less then 15"
            ),
            pytest.param(
                5,
                15,
                [0, 1],
                id="one if dog_age in the range of 15 to 23"
            ),
            pytest.param(
                20,
                14,
                [1, 0],
                id="one if cat_age in the range of 15 to 23"
            ),
            pytest.param(
                23,
                17,
                [1, 1],
                id="one if cat_age or dog_age in the range of 15 to 23"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="cat_age and dog_age is more 23"
            ),
            pytest.param(
                -1, -1, [0, 0],
                id="should return zero if cat/dog age is negative"
            )
        ]
    )
    def test_check_result(
            self,
            cat_age: int,
            dog_age: int,
            expected_age: list

    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_age


class TestExpectedError:
    @pytest.mark.parametrize(
        "dog_age, cat_age, expected_error",
        [
            pytest.param(
                "5",
                0,
                TypeError,
                id="should raise error if values ages is not int"
            )
        ]
    )
    def test_raising_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Type[Exception]
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
