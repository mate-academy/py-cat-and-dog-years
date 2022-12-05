import pytest
from typing import Any
from app.main import get_human_age

# write your code here


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="dog_and_cat_should_be_zero_if_age_is_0"
        ),
        pytest.param(
            -1,
            -2,
            [0, 0],
            id="dog_and_cat_should_be_zero_if_age_is_negative"
        ),
        pytest.param(
            14,
            13,
            [0, 0],
            id="dog_and_cat_should_be_zero_if_age_less_15"
        ),
        pytest.param(
            27,
            28,
            [2, 2],
            id="dog_and_cat_every_nine_years_after_15"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="cat_every_four_years_after_first_fifteen_and_second_9"
        ),
        pytest.param(
            27,
            29,
            [2, 3],
            id="dog_every_fife_years_after_first_fifteen_and_second_9"
        ),
        pytest.param(
            1000,
            1000,
            [246, 197],
            id="should_correctly_calculate_if_large_numbers"
        ),
    ]
)
def test_right_convert_animal_age_to_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:

    assert get_human_age(cat_age, dog_age) == expected_result


def test_type_must_be_integer() -> None:
    with pytest.raises(TypeError):
        get_human_age("cat_age", 11.1)
