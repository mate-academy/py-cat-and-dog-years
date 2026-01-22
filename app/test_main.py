from typing import Any

from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "test when animals 'age' < 0",
        "test when animals 'age' == 0",
        "test must return [0, 0] when age<15",
        "test must return [1, 1] when age=15",
        "test must return [1, 1] when age<24",
        "test must return [2, 2] when age=24",
        "test must return [2, 2] when age=27 and 28",
        "test must return [3, 3] when age=29 and 29",
        "test with big numbers"

    ]
)
def test_get_human_age(cat_age: Any, dog_age: Any, result: Any) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ({4}, {3},),
        ([3], [2],),
        ("0", "45")
    ],
    ids=[
        "raise error when value is dict",
        "raise error when value is list",
        "raise error when value is str"
    ]
)
def test_raise_error_if_value_not_int(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
