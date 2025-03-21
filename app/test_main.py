from typing import Type

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(0, 0, [0, 0], id="should return 0 when age is 0"),
        pytest.param(14, 14, [0, 0], id="should return 0 when age is < 15"),
        pytest.param(23, 23, [1, 1], id="should return 1 when age is < 24"),
        pytest.param(28, 28, [3, 2], id="should calculate differently"),
        pytest.param(28.5, 28.5, [3, 2], id="should round float"),
        pytest.param(-10, -20, [0, 0], id="should return 0 when age is < 0")
    ]
)
def test_calculate_get_human_age(
        cat_age: int,
        dog_age: int,
        result: int
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            "10", "20", TypeError, id="should raise error when age is str"
        ),
        pytest.param(
            [10], [20], TypeError, id="should raise error when age is list"
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
