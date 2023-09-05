import pytest
from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "input_cat_ages, input_dog_ages, expected_values",
    [
        pytest.param(0, -5, [0, 0]),
        pytest.param(14, 14, [0, 0]),
        pytest.param(15, 15, [1, 1]),
        pytest.param(23, 23, [1, 1]),
        pytest.param(24, 24, [2, 2]),
        pytest.param(27, 27, [2, 2]),
        pytest.param(28, 28, [3, 2]),
        pytest.param(100, 100, [21, 17])
    ],
    ids=[
        "zero or negative value should return 0 human years",
        "14 cats/dogs years should return 0 human years",
        "15 cats/dogs years should return 1 human years",
        "23 cats/dogs years should return 1 human years",
        "24 cats/dogs years should return 2 human years",
        "27 cats/dogs years should return 2 human years",
        "28 cats and 28 dogs years should return 3 and 2 human years",
        "100 cats and 100 dogs years should return 21 and 17 human years"
    ]
)
def test_convert_cat_dog_years_into_human_years(
        input_cat_ages: int,
        input_dog_ages: int,
        expected_values: list
) -> None:
    assert get_human_age(input_cat_ages, input_dog_ages) == expected_values


@pytest.mark.parametrize(
    "input_cat_ages, input_dog_ages, expected_error",
    [
        pytest.param(2, "ages", TypeError),
        pytest.param(None, None, TypeError)
    ],
    ids=[
        "should return error if ages are not int type",
        "should return error if ages are not fulfill"
    ]
)
def test_incorrect_type_of_data(
        input_cat_ages: Any,
        input_dog_ages: Any,
        expected_error: Exception) -> None:
    with pytest.raises(expected_error):
        get_human_age(input_cat_ages, input_dog_ages)
