import pytest

from app.main import get_human_age


def test_type_of_returned_data() -> None:
    ages = get_human_age(15, 15)
    assert isinstance(ages, list), "The returned value is not a list"
    assert all(
        isinstance(age, int) for age in ages
    ), "All elements of list is must be an integer"
    assert len(ages) == 2, "The length of the returned list is not 2"


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


def test_get_human_age_with_invalid_input() -> None:
    with pytest.raises(TypeError):
        get_human_age("cat", "dog")
