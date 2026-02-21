import pytest
from typing import Any
from app import main


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age_valid(
    cat_age: int,
    dog_age: int,
    expected_result: list[int]
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 5),
        (5, -1),
        (-10, -10),
    ]
)
def test_get_human_age_value_error(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        main.get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, 15.5),
        (None, 24),
    ]
)
def test_get_human_age_type_error(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)
