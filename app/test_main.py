import pytest
from typing import Type

from app.main import get_human_age

# write your code here


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_cat_age,expected_dog_age",
    [
        pytest.param(0, 0, 0, 0, id="both_zero_age"),
        pytest.param(14, 14, 0, 0, id="below_first_threshold"),
        pytest.param(15, 15, 1, 1, id="first_threshold_reached"),
        pytest.param(23, 23, 1, 1, id="before_second_threshold"),
        pytest.param(24, 24, 2, 2, id="second_threshold_reached"),
        pytest.param(27, 27, 2, 2, id="before_third_threshold"),
        pytest.param(28, 28, 3, 2, id="third_threshold_cat_only"),
        pytest.param(29, 29, 3, 3, id="third_threshold_cat_and_dog"),
        pytest.param(32, 34, 4, 4, id="multiple_extra_years"),
        pytest.param(100, 100, 21, 17, id="very_large_ages"),
    ]
)
def test_correct_conversion_animal_age_to_human(
        cat_age: int,
        dog_age: int,
        expected_cat_age: int,
        expected_dog_age: int,
) -> None:
    assert get_human_age(cat_age, dog_age) == [
        expected_cat_age, expected_dog_age
    ]


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        pytest.param(-1, 15, ValueError, id="negative_cat_age"),
        pytest.param(15, -1, ValueError, id="negative_dog_age"),
        pytest.param("1", "1", AttributeError, id="non_integer_input"),
    ]
)
def test_incorrect_input_raise_error(
        cat_age: int,
        dog_age: int,
        expected_error: Type[Exception]
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
