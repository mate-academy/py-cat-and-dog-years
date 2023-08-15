from typing import Any

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_cat, human_dog",
    [
        (0, 0, 0, 0),
        (14, 14, 0, 0),
        (15, 15, 1, 1),
        (23, 23, 1, 1),
        (24, 24, 2, 2),
        (27, 27, 2, 2),
        (28, 28, 3, 2),
        (100, 100, 21, 17)
    ]
)
def test_check_correct_matches(
        cat_age: int,
        dog_age: int,
        human_cat: int,
        human_dog: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [human_cat, human_dog]


@pytest.mark.parametrize(
    "cat_age, dog_age, error",
    [
        (-5, -23, ValueError),
        (143486, 23592, ValueError),
        ([], [], TypeError),
        ({}, (), TypeError)
    ]
)
def test_check_any_errors(
        cat_age: Any,
        dog_age: Any,
        error: type[Exception]
) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)
