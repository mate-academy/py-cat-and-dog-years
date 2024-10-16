from app.main import get_human_age

import pytest


@pytest.mark.parametrize(
    "cat_age,"
    "dog_age,"
    "human_age", [
        pytest.param(
            14, 14,
            [0, 0],
            id="test_14_years_cat_dog_should_convert_in_0_human_age"
        ),
        pytest.param(
            15, 15,
            [1, 1],
            id="test_15_years_cat_dog_should_convert_in_1_human_age"
        ),
        pytest.param(
            23, 23,
            [1, 1],
            id="test_23_years_cat_dog_should_convert_in_1_human_age"
        ),
        pytest.param(
            24, 24,
            [2, 2],
            id="test_24_24_years_cat_dog_should_convert_in_2_human_age"
        ),
        pytest.param(
            27, 28,
            [2, 2],
            id="test_27_28_years_cat_dog_should_convert_in_2_human_age"
        ),
        pytest.param(
            28, 29,
            [3, 3],
            id="test_28_29_years_cat_dog_should_convert_in_3_human_age"
        )
    ]
)
def test_should_convert_cat_dog_age_to_human_age(
        cat_age: int,
        dog_age: int,
        human_age: int
) -> None:

    assert get_human_age(cat_age, dog_age) == human_age
