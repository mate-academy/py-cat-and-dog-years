import pytest
from typing import Type

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        (-10, -1, 0),
        (0, 0, 0),
        (14, 14, 0),
        (15, 15, 1),
        (23, 23, 1),
        (24, 24, 2),
        (27, 28, 2),
        (28, 29, 3),
    ],
    ids=[
        "negative years should convert to 0",
        "zeros years should convert to 0",
        "14 or less years should convert to 0 human age",
        "15 years should convert to 1 human age",
        "23 or less years should convert to 1 human age",
        "24 years should convert to 2 human age",
        "27/28 cat/dog years should convert to 2 human age",
        "28/29 cat/dog years should convert to 3 human age",
    ]
)
def test_negative_and_normal_values(
        cat_age: int, dog_age: int, expected_result: int
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == [expected_result, expected_result]
    )


@pytest.mark.parametrize(
    "years,expected_result",
    [
        (100, [21, 17]),
        (500, [121, 97]),
        (1_000, [246, 197]),
        (10_000, [2496, 1997]),
        (123_456_789_999, [30_864_197_495, 24_691_357_997])
    ],
)
def test_large_values(
        years: int, expected_result: list[int]
) -> None:
    assert get_human_age(cat_age=years, dog_age=years) == expected_result


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("test", 1),
        (1, "test"),
        ([0], 1),
        (1, [0]),
        ((0,), 1),
        (1, (0,)),
        ({0: 0}, 1),
        (1, {0: 0}),
        ({0}, 1),
        (1, {0}),
        (None, None),
    ]
)
def test_argument_types(
        cat_age: any,
        dog_age: any,
        expected_error: Type[Exception] = TypeError
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
