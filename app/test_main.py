import pytest
from app.main import get_human_age


def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_under_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_first_human_age() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_second_threshould() -> None:
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]


def test_cat_extra_years() -> None:
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]


def test_large_values() -> None:
    assert get_human_age(100, 100) == [21, 17]


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (15, 15, [1, 1]),
    (24, 24, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
])
def test_parametrize(cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected
