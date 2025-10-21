import pytest
from app.main import get_human_age
from typing import List


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
    ids=["00", "14", "15", "23", "24", "27", "28", "100"],
)
def test_examples_from_statement(
        cat_age: int,
        dog_age: int,
        expected: List[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, expected",
    [
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
    ],
    ids=["cat-14", "cat-15", "cat-23", "cat-24"],
)
def test_cat_thresholds(cat_age: int, expected: int) -> None:
    assert get_human_age(cat_age, 0)[0] == expected


@pytest.mark.parametrize(
    "dog_age, expected",
    [
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
    ],
    ids=["dog-14", "dog-15", "dog-23", "dog-24"],
)
def test_dog_thresholds(dog_age: int, expected: int) -> None:
    assert get_human_age(0, dog_age)[1] == expected


@pytest.mark.parametrize(
    "cat_age, expected",
    [
        (27, 2),
        (28, 3),
        (31, 3),
        (32, 4),
        (35, 4),
        (36, 5),
    ],
    ids=["cat-27", "cat-28", "cat-31", "cat-32", "cat-35", "cat-36"],
)
def test_cat_post24_increments(
        cat_age: int,
        expected: int
) -> None:
    assert get_human_age(cat_age, 0)[0] == expected


@pytest.mark.parametrize(
    "dog_age, expected",
    [
        (28, 2),
        (29, 3),
        (33, 3),
        (34, 4),
        (38, 4),
        (39, 5),
    ],
    ids=["dog-28", "dog-29", "dog-33", "dog-34", "dog-38", "dog-39"],
)
def test_dog_post24_increments(
        dog_age: int,
        expected: int
) -> None:
    assert get_human_age(0, dog_age)[1] == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (28, 15, [3, 1]),
        (15, 29, [1, 3]),
        (23, 24, [1, 2]),
        (24, 23, [2, 1]),
        (36, 39, [5, 5]),
    ],
    ids=["28-15", "15-29", "23-24", "24-23", "36-39"],
)
def test_independent_cat_dog_computation(
        cat_age: int,
        dog_age: int,
        expected: List[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
