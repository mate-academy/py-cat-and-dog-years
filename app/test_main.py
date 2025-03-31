import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "input_cat_age ,input_dog_age, expected_output",
    [
        pytest.param(
            28,
            28,
            [3, 2],
            id="output should not be changed"
        ),
        pytest.param(
            -20,
            0,
            [0, 0],
            id="should return zeros when passed negative or zero"
        )
    ]
)
def test_input_and_output(
        input_cat_age: int,
        input_dog_age: int,
        expected_output: list
) -> None:
    assert get_human_age(input_cat_age, input_dog_age) == expected_output


@pytest.mark.parametrize(
    "input_cat_age, input_dog_age, expected_error",
    [
        pytest.param(
            "bad_type",
            None,
            TypeError,
            id="should raise error if incorrect data type passed in"
        )
    ]
)
def test_raising_errors_correctly(
    input_cat_age: int,
    input_dog_age: int,
    expected_error: object
) -> None:
    with pytest.raises(expected_error):
        get_human_age(input_cat_age, input_dog_age)
