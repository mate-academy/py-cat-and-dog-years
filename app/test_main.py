import pytest

from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (23, 23, [1, 1]),
        (36, 36, [5, 4]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (221, 304, [51, 58])

    ],
    ids=[
        "test when animals 'age' < 0",
        "test when animals 'age' == 0",
        "test must return [1, 1] when age<24",
        "test should return different age",
        "test 15 dog and cat years should return 1 human year",
        "test 24 dog and cat years should return 2 human year",
        "test with big numbers"

    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ({0}, {0},),
        ([0], [0],),
        ("{0}", "56")
    ],
    ids=[
        "raise error when value dict",
        "raise error when value list",
        "raise error when value str"
    ]
)
def test_raise_error_if_value_not_int(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
