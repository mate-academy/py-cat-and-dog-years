import pytest
from app.main import get_human_age


def test_negative_ages():
    assert get_human_age(-5, -5) == [0, 0]


def test_zero_ages():
    assert get_human_age(0, 0) == [0, 0]


def test_ages_less_than_15():
    assert get_human_age(12, 10) == [0, 0]


def test_ages_less_than_24():
    assert get_human_age(23, 21) == [1, 1]


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        (30, 30, [3, 3]),
        (32, 32, [4, 3]),
        (35, 37, [4, 4]),
        (40, 45, [6, 6]),
        (48, 48, [8, 6])
    ]
)
def test_ages_greater_than_25(cat_age, dog_age, expected_result):
    assert get_human_age(cat_age, dog_age) == expected_result
