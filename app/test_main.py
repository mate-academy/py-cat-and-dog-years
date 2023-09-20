from typing import Type

import pytest

from app.main import get_human_age


@pytest.mark.parametrize("dog_age,cat_age,expected_result",
                         [
                             (24, 24, [2, 2]),
                             (15, 15, [1, 1]),
                             (28, 28, [3, 2]),
                             (100, 100, [21, 17]),
                             (23, 23, [1, 1]),
                             (0, 0, [0, 0]),
                             (14, 14, [0, 0]),
                             (-15, -15, [0, 0])
                         ],
                         ids=[
                             "test_next_9_dog_and_cat_years",
                             "test_check_add_first_15_dog_and_cat_years",
                             "test_every_4_years_extra_human_year",
                             "test_check_large_num_of_dog_and_cat_years",
                             "test_age is less than primary, expects zero",
                             "test_check_if_years_dog_and_cat_is_zero",
                             "test checks that age is not greater than 15",
                             "test_check_negative_numbers_for_function"
                         ])
def test_check_correctly_test_for_dog_and_cat(
        dog_age: int,
        cat_age: int,
        expected_result: list[int]
) -> None:
    assert get_human_age(dog_age, cat_age) == expected_result


@pytest.mark.parametrize("dog_age, cat_age, expected_error", [
    ([1], [1], TypeError),
    ({1}, {1}, TypeError),
    ((1), (1), TypeError),
    (1, [1], TypeError)
], ids=[
    "test_check_type_error_list",
    "test_check_type_error_set",
    "test_check_type_error_tuples",
    "test_check_for_all_correct_type"
])
def check_correct_type_numbers_for_functions(
        dog_age: dict | list | tuple | set,
        cat_age: dict | list | tuple | set,
        expected_error: Type[TypeError]
) -> None:
    with pytest.raises(expected_error):
        get_human_age(dog_age, cat_age)
