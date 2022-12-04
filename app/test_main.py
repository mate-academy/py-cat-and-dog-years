import pytest
from app.main import get_human_age

# write your code here


@pytest.mark.parametrize(
    "cat_int,dog_int,expected_list",
    [
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
        )
    ]
)
def test_convert_animal_age_to_human_age(
        cat_int,
        dog_int,
        expected_list
        ):

    assert get_human_age(cat_int, dog_int) == expected_list
