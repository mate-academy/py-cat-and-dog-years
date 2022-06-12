import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (15, 15, [1, 1]),
        (18, 18, [1, 1]),
        (23, 23, [1, 1]),
    ]
)
def test_should_return_correct_first_ages(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (27, 28, [2, 2]),
    ]
)
def test_should_return_correct_second_ages(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (28, 29, [3, 3]),
        (40, 40, [6, 5]),
        (100, 100, [21, 17])
    ]
)
def test_should_return_correct_third_and_more_ages(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0])
    ]
)
def test_should_return_zeros(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected
