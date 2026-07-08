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
        "zero age gives zero human years",
        "age below 15 gives zero human years",
        "age of exactly 15 gives 1 human year",
        "age of 23 does not yet reach the second milestone",
        "age of exactly 24 gives 2 human years",
        "incomplete extra-year group is discarded",
        "complete extra-year group gives an extra human year",
        "large realistic age is handled correctly",
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (-1, -1),
        (-100, -100),
    ],
)
def test_get_human_age_with_negative_age_returns_zero(
        cat_age: int, dog_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [0, 0]


def test_get_human_age_with_very_large_numbers() -> None:
    assert get_human_age(1000, 1000) == [246, 197]


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("15", 15),
        (None, 15),
    ],
)
def test_get_human_age_with_incorrect_type_raises_type_error(
        cat_age: int, dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
