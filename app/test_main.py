import pytest
from typing import Any


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (-5, -10, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age_valid_inputs(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    from app.main import get_human_age
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("pietnaście", 15),
        (15, "15"),
        ([15], 15),
        (15, None),
    ]
)
def test_get_human_age_wrong_types(cat_age: Any, dog_age: Any) -> None:
    from app.main import get_human_age
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
