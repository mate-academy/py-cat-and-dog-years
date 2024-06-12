from typing import Any

from app.main import get_human_age

import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-1, 3, [0, 0]),
    ],
    ids=[
        "0 of cat age and 0 of dog age should equal 0, 0 of human ages",
        "14 of cat age and 14 of dog age should equal 0, 0 of human ages",
        "15 of cat age and 15 of dog age should equal 1, 1 of human ages",
        "23 of cat age and 23 of dog age should equal 1, 1 of human ages",
        "24 of cat age and 24 of dog age should equal 2, 2 of human ages",
        "27 of cat age and 27 of dog age should equal 2, 2 of human ages",
        "28 of cat age and 28 of dog age should equal 3, 2 of human ages",
        "100 of cat age and 100 of dog age should equal 21, 17 of human ages",
        "-1 of cat age and 3 of dog age should equal 0, 0 of human ages",
    ]
)
def test_of_human_age_in_cat_age_and_dog_age(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param("a", 3, TypeError, id="Age should be integer"),
        pytest.param(
            [1, 2],
            {"key": 2},
            TypeError,
            id="Both param should be integer"
        ),


    ]
)
def test_of_human_age_in_cat_age_and_dog_age_for_errors(
        cat_age: int,
        dog_age: int,
        expected_error: Any
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
