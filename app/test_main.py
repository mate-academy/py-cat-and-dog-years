from typing import Any

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
    ],
    ids=[
        "zero age gives zero human age",
        "last year of the first stage gives zero human age",
        "first year of the second stage gives one human year",
        "last year of the second stage gives one human year",
        "first year of the extra stage gives two human years",
        "cat and dog still share the same age on the boundary",
        "cat gains an extra year 4 years after dog",
        "dog gains an extra year 5 years after cat",
        "large ages are converted correctly",
    ],
)
def test_get_human_age_valid_values(
        cat_age: int, dog_age: int, expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (-1, 0),
        (0, -1),
        (-5, -5),
    ],
    ids=[
        "negative cat age raises ValueError",
        "negative dog age raises ValueError",
        "both ages negative raise ValueError",
    ],
)
def test_get_human_age_negative_values_raise_value_error(
        cat_age: int, dog_age: int
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("15", 15),
        (15, "15"),
        (15.5, 15),
        (15, 15.5),
        (None, 15),
        (15, None),
        ([15], 15),
        (True, 15),
    ],
    ids=[
        "string cat age raises TypeError",
        "string dog age raises TypeError",
        "float cat age raises TypeError",
        "float dog age raises TypeError",
        "None cat age raises TypeError",
        "None dog age raises TypeError",
        "list cat age raises TypeError",
        "bool cat age raises TypeError",
    ],
)
def test_get_human_age_invalid_type_raises_type_error(
        cat_age: Any, dog_age: Any
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
