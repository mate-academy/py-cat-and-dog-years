import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
    ],
    ids=[
        "Negative cat/dog years should convert into 0",
        "0 cat/dog years should convert into 0 human age",
        "14 cat/dog years should convert into 0 human age.",
        "15 cat/dog years should convert into 1 human age.",
        "23 cat/dog years should convert into 1 human age.",
        "24 cat/dog years should convert into 2 human age.",
        "27/28 cat/dog years should convert into 2 human age.",
        "28/29 cat/dog years should convert into 3 human age.",
    ]
)
def test_get_human_age_convert_years(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("12", 15),
        (12, "15"),
        ([12], 15),
        (12, [15]),
        ((12,), 15),
        (12, (15,)),
        ({12}, 15),
        (12, {15}),
    ],
    ids=[
        "str/int should raise TypeError",
        "int/str should raise TypeError",
        "list/int should raise TypeError",
        "int/list should raise TypeError",
        "tuple/int should raise TypeError",
        "int/tuple should raise TypeError",
        "set/int should raise TypeError",
        "int/set should raise TypeError",
    ]
)
def test_get_human_age_should_raise_correct_error_if_receive_incorrect_type(
        cat_age: Any,
        dog_age: Any
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
