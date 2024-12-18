from typing import Type

import pytest

from app.main import get_human_age


class TestConvertAnimalAgeToHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_age",
        [
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17])
        ],
        ids=[
            "15 cat/dog years should convert into 1 human age.",
            "23 cat/dog years should convert into 1 human age.",
            "24 cat/dog years should convert into 2 human age.",
            "28 cat/dog years should convert into 3/2 human age.",
            "100 cat/dog years should convert into 21/17 human age."
        ]
    )
    def test_convert_animal_age_to_human(
            self,
            cat_age: int,
            dog_age: int,
            human_age: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age

    @pytest.mark.parametrize(
        "cat_age,dog_age,error",
        [
            (0, 0, ValueError),
            (101, 101, ValueError),
            (-1, -1, ValueError),
            ("", "", TypeError)
        ],
        ids=[
            "Cat/Dog years can't be more than 0.",
            "Cat/Dog years can't be not more than 100.",
            "Cat/Dog years can't be negative.",
            "You need to use only int as cat/dog years.",
        ]
    )
    def test_raising_errors(
            self,
            cat_age: int,
            dog_age: int,
            error: Type[ValueError | TypeError]
    ) -> None:
        with pytest.raises(error):
            get_human_age(cat_age, dog_age)
