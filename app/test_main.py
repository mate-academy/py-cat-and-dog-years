from typing import List, Any

import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (-1, 0, [0, 0]),
            (0, -1, [0, 0]),
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
        ],
        ids=[
            "Cat age is negative",
            "Dog age is negative",
            "Both cat and dog ages are zero",
            "Both cat and dog ages are below 15 and result in 0 human ages",
            "Both animals just above 15 years, resulting in 1 human year each",
            "Both animals 15-23 years, resulting in 1 human year each",
            "Both animals just above 23 years, resulting in 2 human years",
            "Cat 24-26 years, 2 human years, dog 1 human year",
            "Cat above 26 years, 3 human years, dog 10 years, 2 human years",
            "Both animals 100 years, 21 human years for cat, 17 for dog",
        ]
    )
    def test_basic_cases(
            self,
            cat_age: int,
            dog_age: int,
            expected: List[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ("-1", 10),
            (10, "1"),
            ("0", 10),
            (10, "0"),
            ("1000", "1000"),
            ("10", 10),
            (10, "10"),
            ([10], 10),
            (10, [10]),
        ],
        ids=[
            "Cat age is a string",
            "Dog age is a string",
            "Cat age is zero",
            "Dog age is zero",
            "Cat & Dog age is a very large number",
            "Cat age is a string representation of a number",
            "Dog age is a string representation of a number",
            "Cat age is a list",
            "Dog age is a list",
        ]
    )
    def test_error_will_be_raised(
        self,
        cat_age: Any,
        dog_age: Any
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
