import pytest

from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(0, 0, [0, 0], id="0 - 0 - [0, 0]"),
        pytest.param(14, 14, [0, 0], id="14 - 14 - [0, 0]"),
        pytest.param(15, 15, [1, 1], id="15 - 15 - [1, 1]"),
        pytest.param(23, 23, [1, 1], id="23 - 23 - [1, 1]"),
        pytest.param(24, 24, [2, 2], id="24 - 24 - [2, 2]"),
        pytest.param(27, 27, [2, 2], id="27 - 27 - [2, 2]"),
        pytest.param(28, 28, [3, 2], id="28 - 28 - [3, 2]"),
        pytest.param(29, 29, [3, 3], id="29 - 29 - [3, 3]"),
        pytest.param(100, 100, [21, 17], id="100 - 100 - [21, 17]"),
        pytest.param(-1, -1, [0, 0], id="-1 - -1 - [0, 0]"),
    ]
)
def test_should_return_correct_values(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,exception",
    [
        pytest.param("0", 0, TypeError, id="str - int - TypeError"),
        pytest.param([0, 1], 0, TypeError, id="list - int - TypeError"),
        pytest.param((0, 0), 1, TypeError, id="tuple - int - TypeError"),
        pytest.param({0: 0, 1: 1}, 0, TypeError, id="dict - int - TypeError"),
        pytest.param(None, 1, TypeError, id="None - int - TypeError"),
        pytest.param(0, "0", TypeError, id="int - str - TypeError"),
        pytest.param(0, [0, 1], TypeError, id="int - list - TypeError"),
        pytest.param(1, (0, 0), TypeError, id="int - tuple - TypeError"),
        pytest.param(0, {0: 0, 1: 1}, TypeError, id="int - dict - TypeError"),
        pytest.param(1, None, TypeError, id="int - None - TypeError"),
    ]
)
def test_should_raise_correct_error(
        cat_age: Any,
        dog_age: Any,
        exception: Any
) -> None:
    with pytest.raises(exception):
        get_human_age(cat_age, dog_age)
