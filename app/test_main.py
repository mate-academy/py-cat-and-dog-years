from typing import Any
import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_check_edge_values(
    cat_age: int,
    dog_age: int,
    human_age: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -1),
        (-5, -5),
    ]
)
def test_check_negative_values(
    cat_age: int,
    dog_age: int
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (10.5, 10),
        (10, 10.5),
        (5.5, 3.3),
        ("ten", 10),
        (10, "ten"),
        ("five", "three"),
        (None, 10),
        (10, None),
        ([10, 15], 10),
        (10, [10, 15]),
    ]
)
def test_check_non_integer_values(
    cat_age: Any,
    dog_age: Any
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
