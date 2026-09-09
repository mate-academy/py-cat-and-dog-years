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
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("10", 10),
        (10, "10"),
        (None, 5),
        (5, [1, 2]),
        ({"age": 3}, 4),
    ],
)
def test_get_human_age_raises_type_error(
    cat_age: Any,
    dog_age: Any,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
