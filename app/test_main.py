from typing import Any, Type
import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 14, [1, 0]),
        (14, 15, [0, 1]),
        (23, 23, [1, 1]),
        (24, 23, [2, 1]),
        (23, 24, [1, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "0/0", "14/14", "15/14", "14/15", "23/23",
        "24/23", "23/24", "27/27", "28/28", "28/29", "100/100"
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_years, dog_years",
    [
        (-1, 5),
        (5, -1),
        (-10, -10),
    ],
    ids=["negative_cat", "negative_dog", "both_negative"]
)
def test_get_human_age_negative_values(cat_years: int, dog_years: int) -> None:
    assert get_human_age(cat_years, dog_years) == [0, 0]


@pytest.mark.parametrize(
    "cat_years, dog_years, exception",
    [
        ("15", 15, TypeError),
        (15, None, TypeError),
        ([24], 24, TypeError),
    ],
    ids=["string_input", "none_input", "list_input"]
)
def test_get_human_age_wrong_types(
    cat_years: Any,
    dog_years: Any,
    exception: Type[BaseException]
) -> None:
    with pytest.raises(exception):
        get_human_age(cat_years, dog_years)
