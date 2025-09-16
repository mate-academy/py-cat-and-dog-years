import pytest
from typing import Any


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        (-5, -20, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
        (10000, 20000, [2496, 3997]),
    ]
)
def test_logic_of_the_function(
    cat_age: int, dog_age: int, human_age: list[int]
) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == human_age
    assert isinstance(result, list)
    assert len(result) == 2
    assert isinstance(result[0], int)
    assert isinstance(result[1], int)


@pytest.mark.parametrize(
    "cat, dog",
    [
        ("cat", "dog"),
        ([4, 5, 3], 6),
        (None, 6,)
    ]
)
def test_ages_are_numbers(cat: Any, dog: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat, dog)


@pytest.mark.parametrize(
    "age_before, age_limit",
    [
        (14, 15),
        (23, 24),
        (27, 28),
    ]
)
def test_cat_age_limits(age_before: int, age_limit: int) -> None:
    human_before = get_human_age(age_before, 0)[0]
    human_limit = get_human_age(age_limit, 0)[0]
    assert human_before != human_limit


@pytest.mark.parametrize(
    "age_before, age_limit",
    [
        (14, 15),
        (23, 24),
        (28, 29),
    ]
)
def test_dog_age_limits(age_before: int, age_limit: int) -> None:
    human_before = get_human_age(0, age_before)[1]
    human_limit = get_human_age(0, age_limit)[1]
    assert human_before != human_limit
