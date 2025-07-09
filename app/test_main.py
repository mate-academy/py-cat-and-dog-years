from app.main import get_human_age

import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
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
def test_human_age_basic_cases(
    cat_age: int, dog_age: int, result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (1000, 1000, [246, 197]),
        (10000, 10000, [2496, 1997]),
    ],
)
def test_human_age_large_values(
    cat_age: int, dog_age: int, result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (27, 29, [2, 3]),
        (28, 30, [3, 3]),
    ],
)
def test_human_age_threshold_transitions(
    cat_age: int, dog_age: int, result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (100, 10, [21, 0]),
        (10, 100, [0, 17]),
    ],
)
def test_human_age_cat_and_dog_uneven(
    cat_age: int, dog_age: int, result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (-1, 10),
        (10, -5),
    ],
)
def test_human_age_negative_values_raises(
    cat_age: int,
    dog_age: int,
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("fifteen", 10),
        (10.5, 20),
        (None, []),
    ],
)
def test_human_age_invalid_type_raises(
    cat_age: int,
    dog_age: int,
) -> None:
    with pytest.raises((TypeError, ValueError)):
        get_human_age(cat_age, dog_age)
