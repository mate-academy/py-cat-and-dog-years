import pytest
from app.main import get_human_age


def test_when_current_year_less_than_first_year():
    assert get_human_age(14, 14) == [0, 0]


def test_when_current_year_equal_first_year():
    assert get_human_age(15, 15) == [1, 1]


def test_when_current_year_less_than_than_sum_of_first_and_second_year():
    assert get_human_age(23, 23) == [1, 1]


def test_when_current_year_greater_than_sum_of_first_and_second_year():
    assert get_human_age(24, 24) == [2, 2]


def test_when_current_years_greater_than_subtract_and_divide():
    assert get_human_age(28, 28) == [3, 2]


def test_if_current_year_unusually_large():
    assert get_human_age(100, 100) == [21, 17]


def test_raises_type_error():
    with pytest.raises(TypeError):
        get_human_age("cat", "dog")


@pytest.mark.parametrize(
    "each_year_cat, each_year_dog, expected", [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_various_human_age(
        each_year_cat: int,
        each_year_dog: int,
        expected) -> None:
    assert get_human_age(each_year_cat, each_year_dog) == expected
