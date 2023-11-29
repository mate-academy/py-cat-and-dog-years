import pytest
from app.main import get_human_age
from typing import Any


@pytest.mark.parametrize(
    "cat_age,dog_age,human_ages",
    [
        (-1, 1, [0, 0]),
        (1, -1, [0, 0]),
        (-1, -1, [0, 0]),
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
def test_should_convert_animal_ages_to_human_ages(
        cat_age: int,
        dog_age: int,
        human_ages: int
) -> None:
    assert get_human_age(cat_age, dog_age) == human_ages


@pytest.mark.parametrize(
    "cat_age,dog_age,error",
    [
        ("0", 0, TypeError),
        (0, None, TypeError),
        ("0", None, TypeError),
    ],
)
def test_should_return_an_error(
        cat_age: Any,
        dog_age: Any,
        error: Any
) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)
