import pytest
from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_ages",
    [
        (14, 14, [0, 0]),
        (23, 23, [1, 1]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "if values less than 15",
        "if values less than 24",
        "if values equal 15",
        "if values equal 24",
        "if values have extra years",
        "if values are large"
    ]
)
def test_should_correct_convert_years(
        cat_age: int,
        dog_age: int,
        expected_ages: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_ages


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        ("5", 15, TypeError),
        (15, [15], TypeError),
        ({2}, 15, TypeError),

    ],
    ids=[
        "should raise error if value is str",
        "should raise error if value is list",
        "should raise error if value is dict",
    ]
)
def test_should_return_correct_exception(
        cat_age: Any,
        dog_age: Any,
        expected_error: Any
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
