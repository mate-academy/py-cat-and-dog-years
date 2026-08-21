import pytest
from app.main import get_human_age


def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_before_first_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_exact_first_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_before_second_human_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_exact_second_human_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_before_third_human_year() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_exact_third_human_year() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_parametrized(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
