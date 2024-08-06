import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (40, 50, [6, 7])
    ],
    ids=[
        "should convert 0 cat/dog years to 0 human years",
        "should convert 14 cat/dog years to 0 human years",
        "should convert 15 cat/dog years to 1 human years",
        "should convert 23 cat/dog years to 1 human years",
        "should convert 24 cat/dog years to 2 human years",
        "should convert 27 cat/dog years to 2 human years",
        "should convert 28 cat/dog years to 3/2 human years",
        "should convert 100 cat/dog years to 21/17 human years",
        "should convert 40 cat/50 dog years to 5/7 human years"
    ]
)
def test_ages(cat_age: int, dog_age: int, human_age: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


def test_negative_ages() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, -1)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (10.5, 20.4),
        (True, False),
        ("10", "10"),
        ([10], [20]),
        ({"cat_age": 20}, {"dog_age": 25}),
        ((25,), (25,)),
        ({25}, {25})
    ],
    ids=[
        "float is invalid type",
        "bool is invalid type",
        "string is invalid type",
        "list is invalid type",
        "dict is invalid type",
        "tuple is invalid type",
        "set is invalid type"
    ]
)
def test_invalid_type(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
