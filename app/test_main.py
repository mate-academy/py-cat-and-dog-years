from typing import Any

import pytest

from app.main import get_human_age


# write your code here
def test_should_return_0_human_years_for_first_14_cat_and_dog_years() -> None:
    for year in range(15):
        assert get_human_age(year, year) == [0, 0]


def test_should_return_1_human_years_from_15_to_23_cat_and_dog_years() -> None:
    for year in range(15, 24):
        assert get_human_age(year, year) == [1, 1]


def test_should_return_2_human_years_for_24_cat_and_dog_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_add_1_human_years_every_4_years_for_a_cat_over_23() -> None:
    assert get_human_age(27, 0)[0] == 2
    assert get_human_age(28, 0)[0] == 3
    assert get_human_age(100, 0)[0] == 21


def test_should_add_1_human_years_every_4_years_for_a_dog_over_23() -> None:
    assert get_human_age(0, 28)[1] == 2
    assert get_human_age(0, 29)[1] == 3
    assert get_human_age(0, 100)[1] == 17


@pytest.mark.parametrize(
    "cat_age,dog_age,error",
    [
        (45, "28", TypeError),
        ("45", 6, TypeError),
        ({45}, 6, TypeError),
        (45, {6}, TypeError),
        (None, 6, TypeError),
        (45, None, TypeError),
    ],
)
def test_should_raise_error_if_arguments_is_not_string(
        cat_age: Any,
        dog_age: Any,
        error: Any
) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)


def test_should_raise_error_if_arguments_is_negative_numbers() -> None:
    assert get_human_age(-45, -45) == [0, 0]


def test_case_with_big_numbers() -> None:
    assert get_human_age(100000, 500000) == [24996, 99997]
