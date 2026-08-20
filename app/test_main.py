from typing import Any
import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "ages,correct_output",
    [
        pytest.param(
            (12, 0),
            [0, 0],
            id="test for 0 ages"
        ),
        pytest.param(
            (29, 30),
            [3, 3],
            id="2 regular ints that are bigger than 15"
        ),
        pytest.param(
            (-5, 398),
            [0, 76],
            id="test for negative and large num"
        ),
    ]
)
def test_func_values(ages: tuple, correct_output: list) -> None:
    cat_age, dog_age = ages
    assert get_human_age(cat_age, dog_age) == correct_output


@pytest.mark.parametrize(
    "cat_age,dog_age,correct_error",
    [
        pytest.param(
            [], "Hello", ValueError, id="test for wrong type of args"
        ),
    ]
)
def test_func_errors(cat_age: Any,
                     dog_age: Any,
                     correct_error: Exception
                     ) -> None:
    with pytest.raises(correct_error):
        get_human_age(cat_age, dog_age)
