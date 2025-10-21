import pytest
from typing import Any
from app.main import get_human_age

cases_zero = [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
]

cases_one = [
    (15, 15, [1, 1]),
    (20, 20, [1, 1]),
    (23, 23, [1, 1]),
]

cases_two = [
    (24, 24, [2, 2]),
    (25, 25, [2, 2]),
    (27, 27, [2, 2]),
]

cases_after_second = [
    (28, 28, [3, 2]),
    (32, 32, [4, 3]),
    (40, 40, [6, 5]),
]

cases_large = [
    (100, 100, [21, 17]),
]

cases_negative = [
    (-1, 10, [0, 1]),
    (-5, -3, [0, 0]),
    (10, -2, [0, 0]),
]

cases_invalid = [
    (15.5, 10),
    ("15", 10),
    (None, 10),
    (15, "10"),
    (15, None),
    ([], 10),
]

cases_dog_thresholds = [
    (29, 2),
    (30, 3),
    (34, 3),
    (35, 4),
]

cases_mixed = [
    (28, 30, [3, 3]),
    (15, 24, [1, 2]),
    (0, 27, [0, 2]),
    (27, 0, [2, 0]),
]


@pytest.mark.parametrize("cat_age, dog_age, expected", cases_zero)
def test_zero_years(cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert (
        get_human_age(cat_age, dog_age) == expected
    )


@pytest.mark.parametrize("cat_age, dog_age, expected", cases_one)
def test_first_stage(cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert (
        get_human_age(cat_age, dog_age) == expected
    )


@pytest.mark.parametrize("cat_age, dog_age, expected", cases_two)
def test_second_stage(cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert (
        get_human_age(cat_age, dog_age) == expected
    )


@pytest.mark.parametrize(
    "cat_age, dog_age, expected", cases_after_second
)
def test_after_second_stage(cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert (
        get_human_age(cat_age, dog_age) == expected
    )


@pytest.mark.parametrize("cat_age, dog_age, expected", cases_large)
def test_large_ages(cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert (
        get_human_age(cat_age, dog_age) == expected
    )


@pytest.mark.parametrize("cat_age, dog_age, expected", cases_negative)
def test_negative_inputs(cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert (
        get_human_age(cat_age, dog_age) == expected
    )


@pytest.mark.parametrize("cat_age, dog_age", cases_invalid)
def test_invalid_types(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize("dog_age, expected", cases_dog_thresholds)
def test_dog_thresholds(dog_age: int, expected: int) -> None:
    assert (
        get_human_age(28, dog_age)[1] == expected
    )


@pytest.mark.parametrize(
    "cat_age, dog_age, expected", cases_mixed
)
def test_mixed_values(cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert (
        get_human_age(cat_age, dog_age) == expected
    )
