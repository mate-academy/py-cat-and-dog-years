from typing import Iterable

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "age,expected_instance,expected_inner_instance,expected_length",
    [
        ([15, 15], list, int, 2)
    ],
    ids=(
        "Check correct instances of output",
    )
)
def test_type_of_returned_data(
        age: list,
        expected_instance: type[Iterable],
        expected_inner_instance: type,
        expected_length: int
) -> None:
    ages = get_human_age(*age)
    assert (
        isinstance(ages, expected_instance)
    ), "The returned value is not a list"
    assert all(
        isinstance(age, expected_inner_instance) for age in ages
    ), "All elements of list is must be an integer"
    assert (
        len(ages) == expected_length
    ), "The length of the returned list is not 2"


@pytest.mark.parametrize(
    "ages,expected",
    [
        ([14, 14], [0, 0]),
        ([15, 15], [1, 1]),
        ([23, 23], [1, 1]),
        ([24, 24], [2, 2]),
        ([27, 28], [2, 2]),
        ([28, 29], [3, 3]),
        ([200, 200], [46, 37]),
        ([340, 210], [81, 39]),
        ([0, 0], [0, 0]),
        ([100, 0], [21, 0]),
        ([0, 100], [0, 17]),
        ([-200, -200], [0, 0])
    ],
    ids=[
        "Cat's and dog's age 14 should return [0, 0]",
        "Cat's and dog's age 15 should return [1, 1]",
        "Cat's and dog's age 23 should return [1, 1]",
        "Cat's and dog's age 24 should return [2, 2]",
        "A cat age 27 and a dog age 28 should return [2, 2]",
        "A cat age 28 and a dog age 29 should return [3, 3]",
        "Cat's and dog's age 200 should return [46, 37]",
        "A cat age 340 and a dog age 210 should return [81, 39]",
        "Cat's and dog's age 0 should return [0, 0]",
        "A cat age 100 and a dog age 0 should return [21, 0]",
        "A cat age 0 and a dog age 100 should return [0, 17]",
        "Cat's and dog's age -200 should return [0, 0]"
    ]

)
def test_correct_data(ages: list, expected: list) -> None:
    assert get_human_age(*ages) == expected


@pytest.mark.parametrize(
    "ages, expected_exception",
    [
        (["cat", "dog"], TypeError),
        ([["cat", "dog"]], TypeError),
        ([{"cat", "dog"}], TypeError),
    ],
    ids=(
        "invalid_input_str",
        "invalid_input_list",
        "invalid_input_set"
    )
)
def test_get_human_age_with_invalid_input(
        ages: list, expected_exception: Exception
) -> None:
    with pytest.raises(expected_exception):
        get_human_age(*ages)
