from app.main import get_human_age

import pytest

from typing import Any


class TestGetHumanAge:

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_ages",
        [
            (-1, -20, [0, 0]),
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (24, 24, [2, 2]),
            (28, 28, [3, 2]),
            (16, 100, [1, 17]),
        ],
        ids=[
            "age is less zero - results equal zero",
            "both ages are equal zero - results equal zero",
            "both ages are less than 15 - results equal zero",
            "both ages are equal 24 - results equal two",
            "both ages are equal - result different",
            "ages are different - result different",
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected_ages: list[int]) -> None:
        assert (get_human_age(cat_age, dog_age) == expected_ages)

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            (2003, "15"),
            ([2003], 15),
            ({2003}, 15),
            ({2003: 2003}, 15),
            ((20, 3), 15),
        ],
        ids=[
            "age must be int - not str",
            "age must be int - not list",
            "age must be int - not set",
            "age must be int - not dict",
            "age must be int - not tuple",
        ]
    )
    def test_invalid_input_data(
            self,
            cat_age: Any,
            dog_age: Any) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
