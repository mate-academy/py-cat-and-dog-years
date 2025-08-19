from app.main import get_human_age
import pytest


def test_both_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_below_first_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_exactly_first_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_between_first_and_second_threshold() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_exactly_second_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_one_before_extra_year() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_first_extra_year_for_cat() -> None:
    assert get_human_age(28, 27) == [3, 2]


def test_large_values() -> None:
    assert get_human_age(100, 100) == [21, 17]


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (16, 16, [1, 1]),
        (25, 25, [2, 2]),
        (29, 30, [3, 3]),
        (40, 40, [6, 5]),
    ],
)
def test_parametrized(cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected
