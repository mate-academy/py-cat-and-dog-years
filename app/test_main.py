from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),

        (15, 15, [1, 1]),
        (15.1, 15.1, [1, 1]),
        (23, 23, [1, 1]),

        (24, 24, [2, 2]),
        (27, 28, [2, 2]),

        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected


def test_should_return_zero_when_ages_are_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_for_15_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_for_24_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_for_28_years() -> None:
    assert get_human_age(28, 28) == [3, 2]
