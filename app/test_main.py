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
        (100, 100, [21, 17]),
    ],
    ids=[
        "zero age should convert into 0 human age",
        "14 cat/dog years should convert into 0 human age",
        "15 cat/dog years should convert into 1 human age",
        "23 cat/dog years should convert into 1 human age",
        "24 cat/dog years should convert into 2 human age",
        "27 cat/dog years should convert into 2 human age",
        "28 cat/dog years should convert into 3/2 human age",
        "100 cat/dog years should convert into 21/17 human age",
    ]
)
def test_should_convert_to_human_age(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_should_return_zero_for_negative_age() -> None:
    assert get_human_age(-1, -100) == [0, 0]


def test_should_convert_very_large_age() -> None:
    assert get_human_age(1_000_000, 1_000_000) == [249_996, 199_997]


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("15", 15),
        (15, None),
        ([15], 15),
    ],
    ids=[
        "string age should raise TypeError",
        "None age should raise TypeError",
        "list age should raise TypeError",
    ]
)
def test_should_raise_type_error_for_non_numeric_age(
        cat_age: object,
        dog_age: object
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
