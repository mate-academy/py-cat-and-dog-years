import pytest

from app.main import get_human_age


def test_type_of_returned_data() -> None:
    ages = get_human_age(15, 15)
    assert isinstance(ages, list), "The returned value is not a list"
    assert isinstance(ages[0], int), "The first element of the returned list is not an integer"
    assert isinstance(ages[1], int), "The second element of the returned list is not an integer"
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
        "Two cats aged 14 should return [0, 0]",
        "Two cats aged 15 should return [1, 1]",
        "Two cats aged 23 should return [1, 1]",
        "Two cats aged 24 should return [2, 2]",
        "A cat aged 27 and a dog aged 28 should return [2, 2]",
        "A cat aged 28 and a dog aged 29 should return [3, 3]",
        "Two animals aged 200 should return [46, 37]",
        "A cat aged 340 and a dog aged 210 should return [81, 39]",
        "Two animals aged 0 should return [0, 0]",
        "A cat aged 100 and a dog aged 0 should return [21, 0]",
        "A cat aged 0 and a dog aged 100 should return [0, 17]",
        "Two animals aged -200 should return [0, 0]"
    ]

)
def test_correct_data(ages: list, expected: list) -> None:
    assert get_human_age(*ages) == expected
