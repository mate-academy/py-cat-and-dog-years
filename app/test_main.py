from typing import List, Any
import pytest
from app import main


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
        (31, 33, [3, 3]),
        (32, 34, [4, 4]),
        (100, 100, [21, 17]),
        (50, 60, [8, 9]),
        (100000, 100000, [24996, 19997]),
    ],
)
def test_get_human_age_combinations(
    cat_age: int,
    dog_age: int,
    expected: List[int],
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


def test_cat_and_dog_different_inputs() -> None:
    assert main.get_human_age(15, 14) == [1, 0]
    assert main.get_human_age(14, 15) == [0, 1]
    assert main.get_human_age(24, 23) == [2, 1]
    assert main.get_human_age(23, 24) == [1, 2]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 5),
        (5, -1),
        (-100, -100),
    ],
)
def test_get_human_age_negative_values(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        main.get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        (1.5, 15),
        (15, 1.5),
        (None, 15),
        (15, None),
        ([15], 15),
    ],
)
def test_get_human_age_invalid_types(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)
