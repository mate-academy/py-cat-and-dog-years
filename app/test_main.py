import pytest

import traceback

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(
            14, 14, [0, 0],
            id="human age should be equal to 0"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="human age should be equal to 1"
        ),
        pytest.param(
            27, 28, [2, 2],
            id="human age should be equal to 2"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="human age should be more than 2"
        ),
        pytest.param(
            - 1, - 1, [0, 0],
            id="test_if_function_receives_negative_number"
        ),
        pytest.param(
            0, 0, [0, 0],
            id="test_if_function_receives_zero"
        ),
        pytest.param(
            1000, 1000, [246, 197],
            id="test_if_function_receives_really_large_numbers"
        )
    ]
)
def test_correct_return(cat_age: int,
                        dog_age: int,
                        expected_result: list
                        ) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        pytest.param(
            "cat",
            "dog",
            TypeError,
            id="String_type_error"
        ),
        pytest.param(
            None,
            None,
            TypeError,
            id="None_type_error"
        )
    ]
)
def test_correct_value(cat_age: int,
                       dog_age: int,
                       expected_error: traceback) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
