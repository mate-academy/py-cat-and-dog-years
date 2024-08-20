from typing import Any

import pytest

from app.main import get_human_age


class TestGetHumanAge:

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (0, 0, [0, 0]),
            (-1, -1, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (25, 25, [2, 2]),
            (28, 29, [3, 3]),
            (32, 34, [4, 4]),
            (90, 90, [18, 15]),
        ],
        ids=[
            "Zero age",
            "cat/dog age can not be negative",
            "14 cat/dog years should convert into 0 human age.",
            "15 cat/dog years should convert into 1 human age.",
            "23 cat/dog years should convert into 1 human age.",
            "25 cat/dog years should convert into 2 human age.",
            "28/29 cat/dog years should convert into 3 human age.",
            "32/34 cat/dog years should convert into 4 human age.",
            "Max cat/dog years value",
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ("cat_age", "dog_age"),
            ({5}, {15}),
            ([5], [15]),
            ((5,), (15,)),
        ],
        ids=[
            "cat/dog age must be int not str",
            "cat/dog age must be int not dict",
            "cat/dog age must be int not list",
            "cat/dog age must be int not tuple",
        ]

    )
    def test_get_human_age_typeerror(self, cat_age: Any, dog_age: Any) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
