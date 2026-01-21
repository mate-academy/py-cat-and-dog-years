from typing import Any

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(
            -1, -1, [0, 0],
            id="should return 0 for negative pet age"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="should return 0 for both pets ages "
               "if cat and dogs age less than 15"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="should return 1 for both pets ages "
               "if cat and dogs age less than 23"
        ),
        pytest.param(
            32, 29, [4, 3],
            id="should return correct age for 3-rd or greater pet age"
        ),
        pytest.param(
            27, 28, [2, 2],
            id="should return correct age for 3-rd or greater pet age"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="Test big number"
        )
    ]
)
def test_should_correctly_convert_cat_dogs_years_to_human(
        cat_age: int,
        dog_age: int,
        expected_result: list[int, int]
) -> None:
    result = get_human_age(cat_age, dog_age)

    assert result == expected_result


@pytest.mark.parametrize(
    "age",
    [
        "1",
        [1],
        {"age": 1}
    ]
)
def test_raises_correct_exception_for_wrong_arguments_types(age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(age, age)
