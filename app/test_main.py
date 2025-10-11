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
            (31, 0, [3, 0]),
            (32, 0, [4, 0]),
            (32, 0, [4, 0]),
            (36, 0, [5, 0]),
            (40, 0, [6, 0]),
            (0, 29, [0, 3]),
            (0, 30, [0, 3]),
            (0, 35, [0, 4]),
            (0, 40, [0, 5]),
        ],
        ids=[
            "cat/dog 14 years → [0, 0]",
            "cat/dog 15 years → [1, 1]",
            "cat/dog 23 years → [1, 1]",
            "cat/dog 24 years → [2, 2]",
            "cat/dog 27 years → [2, 2]",
            "cat 27 / dog 30 years → [2, 3]",
            "cat/dog 28 years → [3, 2]",
            "cat 28 / dog 29 years → [3, 3]",
            "cat/dog 100 years → [21, 17]",
            "cat/dog 0 years → [0, 0]",
            "cat/dog 1 year → [0, 0]",
            "cat -1 / dog 15 years → [0, 1]",
            "cat 15 / dog -1 years → [1, 0]",
            "cat/dog 1000 years → [246, 197]",
            "cat 31 / dog 0 years (cat threshold, no change) → [3, 0]",
            "cat 32 / dog 0 years (cat threshold, +1) → [4, 0]",
            "cat 32 / dog 0 years (cat step) → [4, 0]",
            "cat 36 / dog 0 years (cat step) → [5, 0]",
            "cat 40 / dog 0 years (cat step) → [6, 0]",
            "cat 0 / dog 29 years (dog threshold, no change) → [0, 3]",
            "cat 0 / dog 30 years (dog threshold, +1) → [0, 4]",
            "cat 0 / dog 35 years (dog step) → [0, 5]",
            "cat 0 / dog 40 years (dog step) → [0, 6]",
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
