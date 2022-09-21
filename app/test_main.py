from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error_in_list",
    [
        pytest.param(
            0, 0,
            [0, 0],
            id="should return 0 if age is 0"
        ),
        pytest.param(
            14, 14,
            [0, 0],
            id="should return 0 if age less than 15"
        ),
        pytest.param(
            15, 15,
            [1, 1],
            id="should return 1 if age equals to 15"
        ),
        pytest.param(
            13, 15,
            [0, 1],
            id="should return 0 when age is less than first border"
        ),
        pytest.param(
            23, 24,
            [1, 2],
            id="should return 2 if second border more than first border"
        ),
        pytest.param(
            28, 27,
            [3, 2],
            id="should return 3 if first border more than second border"
        ),
        pytest.param(
            28, 28,
            [3, 2],
            id="should 2 in second border if they are equal"
        ),
        pytest.param(
            28, 29,
            [3, 3],
            id="should return 3 when ages are equal third year"
        ),
        pytest.param(
            38, 34,
            [5, 4],
            id="should return correct age when input is above third border"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="should_return_correct_value_with_ages_bigger_than_third_year"
        ),
    ]
)
def test_return_right_age(cat_age, dog_age, expected_error_in_list):
    assert get_human_age(cat_age, dog_age) == expected_error_in_list
