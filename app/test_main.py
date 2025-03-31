from typing import Type

import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(0, 0, [0, 0], id="should return 0 when age is 0"),
        pytest.param(14, 14, [0, 0], id="should return 0 when age < 15"),
        pytest.param(23, 23, [1, 1], id="should return 1 when 15 <= age < 24"),
        pytest.param(27, 27, [2, 2], id="should return 2 when 24 <= age < 28"),
        pytest.param(28, 28, [3, 2], id="should return different result"),
        pytest.param(100.5, 100.5, [21, 17], id="should return round result"),
        pytest.param(-5, -15, [0, 0], id="should return 0 when age < 0"),
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: int) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            "10", "20",
            TypeError,
            id="should raise error when age is str"
        ),
        pytest.param(
            {"Cat": 25}, {"Dog": 10},
            TypeError,
            id="should raise error when age is dict"
        )
    ]
)
def test_raising_errors_correctly(
        cat_age: int,
        dog_age: int,
        expected: Type[Exception]
) -> None:
    with pytest.raises(expected):
        get_human_age(cat_age, dog_age)
