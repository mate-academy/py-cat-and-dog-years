from typing import Any
import pytest
import app.main


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
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
        (100, 14, [21, 0]),
        (14, 100, [0, 17]),
    ],
)
def test_get_human_age_valid_inputs(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert app.main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -1),
    ],
)
def test_get_human_age_negative_ages(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        app.main.get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        (15.5, 15),
        (15, 15.5),
        (None, 15),
        (15, None),
    ],
)
def test_get_human_age_invalid_types(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        app.main.get_human_age(cat_age, dog_age)
