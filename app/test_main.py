import pytest
from typing import Any

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (27, 30, [2, 3]),
            (28, 28, [3, 2]),
            (28, 29, [3, 3]),
            (100, 100, [21, 17]),
            (0, 0, [0, 0]),
            (1, 1, [0, 0]),
            (-1, 15, [0, 1]),
            (15, -1, [1, 0]),
            (1000, 1000, [246, 197]),
        ],
        ids=[
            "14 cat/dog years should convert into 0 human age.",
            "15 cat/dog years should convert into 1 human age.",
            "23 cat/dog years should convert into 1 human age.",
            "24 cat/dog years should convert into 2 human age.",
            "27 cat/dog years should convert into 2 human age.",
            "27/30 cat/dog years should convert into 2 and 3 human age.",
            "28/28 cat/dog years should convert into 3 and 2 human age.",
            "28/29 cat/dog years should convert into 3 human age.",
            "100 cat/dog years should convert into 21 and 17 human age.",
            "0 cat/dog years should convert into 0 human age.",
            "1 cat/dog years should convert into 0 human age.",
            "-1 cat years should convert into 0 human age.",
            "-1 dog years should convert into 0 human age.",
            "1000 cat/dog years should convert into 246 and 197 human age."
        ]
    )
    def test_get_human_age_return_correct_values(self,
                                                 cat_age: int,
                                                 dog_age: int,
                                                 expected: list[int]) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ("string", 5),
            (5, "string"),
            (None, 5),
            (5, None),
            ([], 5),
            (5, {}),
        ],
        ids=[
            "cat_age is a string",
            "dog_age is a string",
            "cat_age is None",
            "dog_age is None",
            "cat_age is a list",
            "dog_age is a dict",
        ]
    )
    def test_get_human_age_type_error(self,
                                      cat_age: Any,
                                      dog_age: Any) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
