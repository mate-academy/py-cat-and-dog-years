import pytest
from typing import List, Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_age",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="should return list of zeroes if animals "
               "ages are zeroes"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="should return list of zeroes if animals "
               "ages are less than or equal 14"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="should return list of ones if animals "
               "ages are greater than or equal 15"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="should return list of ones if animals "
               "ages are less than or equal 23"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="should return list of twos if animals "
               "ages are greater than or equal 24"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="should return list of twos if animals "
               "ages are less than or equal 23"
        ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="should return list of threes if animals "
               "ages are greater than or equal 28 and 29"
        )
    ]
)
def test_convert_age_correctly(
        cat_age: int,
        dog_age: int,
        expected_age: List[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param(
            "cat",
            "dog",
            TypeError
        )
    ]
)
def test_should_raise_error_if_params_are_not_integer(
        cat_age: Any,
        dog_age: Any,
        expected_error: TypeError
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
