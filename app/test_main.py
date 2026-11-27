import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
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
    ]
)
def test_check_cat_and_dog_years(cat_age: int,
                                 dog_age: int,
                                 human_age: list) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize("cat_age,dog_age", [(-1, 0), (0, -5), (-100, -100)])
def test_negative_age_raises(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize("cat_age,dog_age", [
    ("5", 5), (5, None), (1.5, 5), (True, 5),
])
def test_wrong_type_raises(cat_age: int | Any, dog_age: int | Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
