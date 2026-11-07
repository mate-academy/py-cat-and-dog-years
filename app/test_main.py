from typing import Any

import pytest

from app.main import get_human_age


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
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_valid_values(
        cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age", [(-5, -5), (-100, -50)])
def test_get_human_age_negative_values(cat_age: int, dog_age: int) -> None:
    assert get_human_age(cat_age, dog_age) == [0, 0]


def test_get_human_age_very_large_values() -> None:
    assert get_human_age(1000, 1000) == [246, 197]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [("15", 10), (10, "15"), (15.5, 10), (10, [15])],
)
def test_get_human_age_invalid_type_raises_type_error(
        cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
