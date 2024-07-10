import pytest

from typing import Type
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat, dog, result",
    [
        (-13, -13, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "Should return 0 if 0 > age",
        "Should return 0 if age == 0",
        "Should return 0 if 15 > age",
        "Should return 1 if 24 > age > 14",
        "Should return 2 if 28 > age > 23",
        "Should return 3 if cat_age == 28",
        "Should return age > 28 according to converter recommendations"
    ]
)
def test_should_return_the_correct_age(
        cat: int,
        dog: int,
        result: list
) -> None:
    assert get_human_age(cat, dog) == result


@pytest.mark.parametrize(
    "cat, dog, exception",
    [
        ("not_integer", "not_integer", TypeError),
        ("not_integer", 13, TypeError),
        (13, "not_integer", TypeError)
    ],
    ids=[
        "Should except TypeError if both param is not integer",
        "Should except TypeError if first param is not integer",
        "Should except TypeError if second param is not integer"
    ]
)
def test_should_except_correct_exception(
        cat: int,
        dog: int,
        exception: Type[Exception]
) -> None:
    with pytest.raises(exception):
        get_human_age(cat, dog)
