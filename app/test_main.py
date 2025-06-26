import pytest
from app.main import get_human_age


def test_both_zero_years():
    assert get_human_age(0, 0) == [0, 0]


def test_just_below_first_year_threshold():
    assert get_human_age(14, 14) == [0, 0]


def test_exactly_first_year_threshold():
    assert get_human_age(15, 15) == [1, 1]


def test_just_below_second_year_threshold():
    assert get_human_age(23, 23) == [1, 1]


def test_exactly_second_year_threshold():
    assert get_human_age(24, 24) == [2, 2]


def test_between_second_and_third_threshold_cat_extra_year():
    assert get_human_age(28, 28) == [3, 2]


def test_large_ages():
    assert get_human_age(100, 100) == [21, 17]


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (28, 28, [3, 2]),
    (32, 32, [4, 3]),
    (36, 36, [5, 4]),
    (100, 100, [21, 17]),
])
def test_various_cases(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected
