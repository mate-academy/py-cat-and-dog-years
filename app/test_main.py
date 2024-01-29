import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-1, -1, [0, 0])
    ],

    ids=[
        "0 cat/dog should convert into [0, 0]",
        "14 cat/dog should convert into [0, 0]",
        "15 cat/dog should convert into [1, 1]",
        "23 cat/dog should convert into [1, 1]",
        "24 cat/dog should convert into [2, 2]",
        "27 cat/dog should convert into [2, 2]",
        "28 cat/dog should convert into [3, 2]",
        "100 cat/dog should convert into [21, 17]",
        "-1 cat/dog should convert into [0, 0]"
    ]
)
def test_for_get_human_age_with_correct_input(
        cat_years: int,
        dog_years: int,
        expected: list) -> None:
    assert get_human_age(cat_years, dog_years) == expected


@pytest.mark.parametrize(
    "cat_years, dog_years, expected",
    [
        ("12", 9, TypeError)
    ],
    ids=[
        "All values must be INT type"
        ]
)
def test_for_get_human_age_with_uncorrect_input(
        cat_years: Any,
        dog_years: Any,
        expected: Any) -> None:
    with pytest.raises(expected):
        get_human_age(cat_years, dog_years)
