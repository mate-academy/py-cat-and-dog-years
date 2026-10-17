import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
        (-1, -1, [0, 0]),
        (1000, 1000, [246, 197]),
    ],
    ids=[
        "zero ages should convert into 0 human age",
        "14 cat/dog years should convert into 0 human age",
        "15 cat/dog years should convert into 1 human age",
        "23 cat/dog years should convert into 1 human age",
        "24 cat/dog years should convert into 2 human age",
        "27 cat/dog years should convert into 2 human age",
        "28 cat years should convert into 3, dog into 2 human age",
        "29 dog years should convert into 3 human age",
        "100 cat/dog years should convert into 21/17 human age",
        "negative ages should convert into 0 human age",
        "large ages should be converted correctly",
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("15", 15),
        (15, "15"),
        (None, 15),
        ([15], 15),
    ],
    ids=[
        "string cat age should raise TypeError",
        "string dog age should raise TypeError",
        "None cat age should raise TypeError",
        "list cat age should raise TypeError",
    ]
)
def test_incorrect_type_raises_error(cat_age: object, dog_age: object) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
