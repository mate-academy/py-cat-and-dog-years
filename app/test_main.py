from app.main import get_human_age
import pytest


@pytest.mark.parametrize("cat_age,dog_age,expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
])
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_different_cat_and_dog_ages() -> None:
    assert get_human_age(100, 50) == [21, 7]
    assert get_human_age(50, 100) == [8, 17]


def test_negative_ages() -> None:
    assert get_human_age(-5, -10) == [0, 0]


def test_very_large_ages() -> None:
    assert get_human_age(1000, 1000) == [246, 197]
