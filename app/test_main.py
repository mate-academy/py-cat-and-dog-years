from typing import Any

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_output",
    [
        (0, 0, [0, 0]),
        (0, 15, [0, 1]),
        (15, 0, [1, 0]),
        (-1, -1, [0, 0]),
        (-1, 15, [0, 1]),
        (15, -1, [1, 0]),
        (1000000, 15, [249996, 1]),
        (15, 1000000, [1, 199997]),
        (1000000, 1000000, [249996, 199997]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_output: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_output


@pytest.mark.parametrize(
    "invalid_input",
    [
        str,
        float,
        list,
        set,
        dict,
        tuple,
        None,
    ]
)
def test_should_raise_error_if_input_is_not_int(invalid_input: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(invalid_input, 15)
    with pytest.raises(TypeError):
        get_human_age(15, invalid_input)
