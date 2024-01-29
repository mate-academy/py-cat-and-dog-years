import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, expected, ids",
    [
        (0, 0, [0, 0], "0 cat/dog should convert into [0, 0]"),
        (14, 14, [0, 0], "first year for both starts from 15"),
        (15, 15, [1, 1], "15 cat/dog should convert into [1, 1]"),
        (23, 23, [1, 1], "23 cat/dog should convert into [1, 1]"),
        (24, 24, [2, 2], "second year for both starts "
                         "from next 9 years after first 15"),
        (27, 27, [2, 2], "27 cat/dog should convert into [2, 2]"),
        (28, 28, [3, 2], "for cats, every next human year equal to 4,"
                         " and dogs to 5, so there is a difference"),
        (100, 100, [21, 17], "100 cat/dog should convert into [21, 17]"),
        (-1, -1, [0, 0], "-1 cat/dog should convert into [0, 0]")
    ]
)
def test_for_get_human_age_with_correct_input(
        cat_years: int,
        dog_years: int,
        expected: list,
        ids: str) -> None:
    assert get_human_age(cat_years, dog_years) == expected, ids


@pytest.mark.parametrize(
    "cat_years, dog_years, expected, ids",
    [
        ("12", 9, TypeError, "All values must be INT type")
    ]
)
def test_for_get_human_age_with_uncorrect_input(
        cat_years: Any,
        dog_years: Any,
        expected: Any,
        ids: str) -> None:
    with pytest.raises(expected):
        get_human_age(cat_years, dog_years)
