import pytest
from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (-1, 2, [0, 0]),
        (7, -2, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (15, 24, [1, 2]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_can_get_human_age(cat_age: int, dog_age: int, result: list) -> None:
    expected = get_human_age(cat_age, dog_age)
    assert isinstance(expected, list)
    assert len(expected) == 2
    assert (isinstance(obj, int) for obj in expected)
    assert result == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (7, "8"),
        ("7", 8),
        ([2], (5, 3)),
        ({1}, {2: 6})
    ]
)
def test_invalid_types(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
