from typing import Type

import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,cat_dog_human_age",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
            (-1, -1, [0, 0]),
        ],
        ids=[
            "0 cat/dog years should convert into 0 human age.",
            "14 cat/dog years should convert into 0 human age.",
            "15 cat/dog years should convert into 1 human age.",
            "23 cat/dog years should convert into 1 human age.",
            "24 cat/dog years should convert into 2 human age.",
            "27 cat/dog years should convert into 2 human age.",
            "28 cat/dog years should convert into 3/2 human age.",
            "100/100 cat/dog years should convert into 21/17 human age.",
            "Negative cat/dog years should convert into 0/0 human age.",
        ]
    )
    def test_ages(
            self, cat_age: int, dog_age: int, cat_dog_human_age: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == cat_dog_human_age

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_exception",
        [
            ([1], 2, TypeError),
            (12, (12,), TypeError),
        ],
        ids=[
            "Should except TypeError if cat_age is not integer",
            "Should except TypeError if dog_age is not integer",
        ]
    )
    def test_should_except_correct_exception(
            self,
            cat_age: int,
            dog_age: int,
            expected_exception: Type[Exception]
    ) -> None:
        with pytest.raises(expected_exception):
            get_human_age(cat_age, dog_age)
