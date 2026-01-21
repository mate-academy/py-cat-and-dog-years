from typing import Type
import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 28, [2, 2]),
    (28, 29, [3, 3]),
    (0, 0, [0, 0]),
    (-28, -29, [0, 0]),
    (999435, 2333254, [249854, 466648]),
])
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_exception", [
        ("str", "str", TypeError),
        (["str"], ["str"], TypeError),
        ({15: 15}, {2: 2}, TypeError),
    ],
    ids=[
        "string argument is invalid",
        "list argument is invalid",
        "dict argument is invalid"
    ]
)
def test_invalid_input_error(
        cat_age: Type[any],
        dog_age: Type[any],
        expected_exception: Type[Exception]
) -> None:
    with pytest.raises(expected_exception):
        get_human_age(cat_age, dog_age)
