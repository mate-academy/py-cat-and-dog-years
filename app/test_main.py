import pytest
from app.main import get_human_age
from typing import Type


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (0, 0, [0, 0]),
        (100000, 100000, [24996, 19997]),
        (-1, -5, [0, 0])
    ],
    ids=[
        "14 cat/dog years should convert into 0 human age.",
        "15 cat/dog years should convert into 1 human age.",
        "23 cat/dog years should convert into 1 human age.",
        "24 cat/dog years should convert into 2 human age.",
        "0 cat/dog years should convert into 0 human age.",
        "100000 cat/dog years should convert into 24996 / 19997 human age.",
        "cat/dog years cannot be negative"
    ]
)
def test_cat_and_dog_into_human_age(
        cat_age: int, dog_age: int, expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_exception",
    [
        ("20", "20", TypeError),
        ([15], [15], TypeError),
        ({23: 23}, {23: 23}, TypeError),
    ],
    ids=[
        "cat/dog years cannot be string",
        "cat/dog years cannot be list",
        "cat/dog years cannot be dict"
    ]
)
def test_invalid_input_error(
        cat_age: Type[any],
        dog_age: Type[any],
        expected_exception: Type[Exception]
) -> None:
    with pytest.raises(expected_exception):
        get_human_age(cat_age, dog_age)
