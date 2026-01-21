from typing import Type

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="zeros should equal zeros"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="values less than 15 don't count"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="values from 15 to 24 should count as 1"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="values from 24 to 28 count as 2 for both"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="for cat age 28 counts as 3, when for dog it still 2"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id=("for cats after 24, counts as 1 every 4 years "
                "when for dogs every 5 years")
        ),
        pytest.param(
            -1,
            -1,
            [0, 0],
            id="if function gets negative numbers"
        )
    ]
)
def test_can_sum(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        ("1", 1, TypeError),
        (1, "1", TypeError),
        ((), (), TypeError),
        ((), {}, TypeError),
        ([1], (), TypeError),
    ]
)
def test_get_correct_types(
        cat_age: int,
        dog_age: int,
        expected_error: Type[Exception]
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
