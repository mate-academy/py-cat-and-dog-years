import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(-1, -1, [0, 0]),
        pytest.param(0, 0, [0, 0]),
        pytest.param(14, 14, [0, 0]),
        pytest.param(15, 15, [1, 1]),
        pytest.param(23, 23, [1, 1]),
        pytest.param(24, 24, [2, 2]),
        pytest.param(27, 27, [2, 2]),
        pytest.param(28, 28, [3, 2]),
        pytest.param(100, 100, [21, 17])
    ],
    ids=[
        "-1 cat/dog should convert into [0, 0]",
        "0 cat/dog should convert into [0, 0]",
        "14 cat/dog should convert into [0, 0]",
        "15 cat/dog should convert into [1, 1]",
        "23 cat/dog should convert into [1, 1]",
        "24 cat/dog should convert into [2, 2]",
        "27 cat/dog should convert into [2, 2]",
        "28 cat/dog should convert into [3, 2]",
        "100 cat/dog should convert into [21, 17]",
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    )


@pytest.mark.parametrize(
    "cat_age, dog_age, exception",
    [
        pytest.param(5, "5", TypeError),
        pytest.param("5", 5, TypeError)
    ],
    ids=[
        "cats/dogs age is negative number, must be positive",
        "cats/dogs age is str, must be int"
    ]
)
def test_should_raise_error_if_age_is_not_int(
        cat_age: Any,
        dog_age: Any,
        exception: Any

) -> None:
    with pytest.raises(exception):
        get_human_age(cat_age, dog_age)
