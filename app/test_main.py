import pytest
from app.main import get_human_age

from typing import Any


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        (-10, -10, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "Negative animal ages should return [0, 0]",
        "0 animal ages should return [0, 0]",
        "If animal ages less than 15 should return [0, 0]",
        "If animal ages equal 15 should return [1, 1]",
        "If animal ages equal 23 should return [1, 1]",
        "If animal ages equal 24 should return [2, 2]",
        "If animal ages equal 28 should return [3, 2]",
        "If animal ages equal 100 should return [21, 17]",
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        ("12", 12, TypeError),
        (5, [5, 0], TypeError),
        (1, (1,), TypeError),
        ({5: 0}, 5, TypeError)
    ],
    ids=[
        "Animal ages should be type 'int', not 'str'",
        "Animal ages should be type 'int', not 'list'",
        "Animal ages should be type 'int', not 'tuple'",
        "Animal ages should be type 'int', not 'dict'"
    ]
)
def test_get_human_age_raises_the_correct_exception(
        cat_age: Any,
        dog_age: Any,
        expected_error: type[Exception]
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
