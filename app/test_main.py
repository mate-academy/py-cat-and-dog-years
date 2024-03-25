import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_input,dog_input,cat_output,dog_output",
    [
        (0, 0, 0, 0),
        (0.1, 0.1, 0, 0),
        (-999, -999, 0, 0),
        (100, 100, 21, 17),
        (27, 28, 2, 2),
        (28, 29, 3, 3),
        (14.9, 14.9, 0, 0),
        (15, 15, 1, 1)
    ],
    ids=[
        "0 years should convert into 0 years",
        "Decimal numbers should be converted into int values",
        "Negative numbers should be converted into zeros",
        "100/100 cat/dog years should convert into 21/17 human age.",
        "27/28 cat/dog years should convert into 2 human age.",
        "28/29 cat/dog years should convert into 3 human age.",
        "14.9 cat/dog years should be converted into 1 human age (not rounded)",
        "15 cat/dog years should convert into 1 human age."
    ]
)
def test_cat_dog_age_check_valid_data(
        cat_input: int | float,
        dog_input: int | float,
        cat_output: int,
        dog_output: int
) -> None:
    assert get_human_age(cat_input, dog_input) == [cat_output, dog_output]


@pytest.mark.parametrize(
    "cat_input,dog_input,expected_error",
    [
        ("x", "y", TypeError),
        ([1, 2, 3], [4, 5, 6], TypeError),
        ({"x": 1}, {"y": 2}, TypeError),
        (lambda a, b: a * b, lambda a, b: a / b, TypeError)
    ],
    ids=[
        "String as a parameter should throw a TypeError error",
        "List as a parameter should throw a TypeError error",
        "Dictionary as a parameter should throw a TypeError error",
        "Function as a parameter should throw a TypeError error"
    ]
)
def test_cat_dog_age_errors(
        cat_input: any,
        dog_input: any,
        expected_error: Exception
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_input, dog_input)
