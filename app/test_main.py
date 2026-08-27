import pytest

from app import main


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (32, 34, [4, 4]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


def test_cat_and_dog_different_ages() -> None:
    assert main.get_human_age(28, 34) == [3, 4]


def test_zero_cat_age() -> None:
    assert main.get_human_age(0, 50) == [0, 7]


def test_zero_dog_age() -> None:
    assert main.get_human_age(50, 0)[1] == 0


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-5, 10, [0, 0]),
        (-1, 10, [0, 0]),
        (10, -5, [0, 0]),
        (10, -1, [0, 0]),
    ],
)
def test_negative_ages(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected
