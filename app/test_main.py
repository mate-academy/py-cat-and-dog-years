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
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
        (-1, -1, [0, 0]),
    ],
    ids=[
        "zero years should convert into 0 human age",
        "14 years should convert into 0 human age",
        "15 years should convert into 1 human age",
        "23 years should convert into 1 human age",
        "24 years should convert into 2 human age",
        "27 years should convert into 2 human age",
        "28 years: cat gets 3, dog stays 2",
        "29 years should convert into 3 human age",
        "large age should convert correctly",
        "negative age should convert into 0 human age",
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("15", 15),
        (15, "15"),
        (None, 15),
    ],
    ids=[
        "string cat age should raise TypeError",
        "string dog age should raise TypeError",
        "None age should raise TypeError",
    ]
)
def test_get_human_age_raises_type_error(
        cat_age: object,
        dog_age: object
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
