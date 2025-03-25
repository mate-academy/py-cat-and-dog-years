from app.main import get_human_age
from typing import List

import pytest


def test_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_below_first_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_at_first_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_below_second_threshold() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_at_second_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_after_second_threshold() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_different_third_period() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_age() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_cat_boundaries() -> None:
    assert get_human_age(16, 0) == [1, 0]
    assert get_human_age(25, 0) == [2, 0]
    assert get_human_age(28, 0) == [3, 0]


def test_dog_boundaries() -> None:
    assert get_human_age(0, 16) == [0, 1]
    assert get_human_age(0, 25) == [0, 2]
    assert get_human_age(0, 29) == [0, 3]
    assert get_human_age(0, 30) == [0, 3]


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (19, 19, [1, 1]),
    (32, 32, [4, 3]),
    (15, 24, [1, 2]),
    (24, 15, [2, 1]),
])
def test_various_combinations(cat_age: int, dog_age: int,
                              expected: List[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected
