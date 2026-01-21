import pytest
from app.main import get_human_age
from typing import Type


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (-5, 17, [0, 1]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17])
    ],
    ids=[
        "value_is_negative",
        "cat_and_dog_years_are_zeros_values",
        "cat_and_dog_years_less_than_1_human_year",
        "edge_entry_values_for_1_human_years",
        "edge_exit_values_for_1_human_years",
        "edge_entry_values_for_2_human_years",
        "edge_exit_values_for_2_human_years",
        "edge_entry_values_for_3_human_years",
        "cat_and_dog_years_more_than_3_human_years"
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list[int]) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), f"Conversion of {cat_age} and {dog_age} should be equal to {result}"


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        ("20", 50, TypeError),
        (20, [50], TypeError),
        ((20, 50), {20: 50}, TypeError)
    ],
    ids=[
        "raise_type_error_if_years_is_string",
        "raise_type_error_if_years_is_list",
        "raise_type_error_if_years_is_tuple_or_dictionary"
    ]
)
def test_raises_error_correctly(
        cat_age: int,
        dog_age: int,
        expected_error: Type[Exception]
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
