import pytest
from app.main import get_human_age


def test_output_type():
    assert type(get_human_age(1, 1)) == list
    assert all([isinstance(value, int) for value in get_human_age(30, 31)])


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (2, 2, [0, 0]),
        (10, 10, [0, 0]),
        (14, 14, [0, 0])
    ]
)
def test_first_age(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (15, 15, [1, 1]),
        (20, 20, [1, 1]),
        (23, 23, [1, 1])
    ]
)
def test_second_age(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (24, 24, [2, 2]),
        (28, 29, [3, 3]),
        (108, 114, [23, 20])
    ]
)
def test_age_over_two(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected
