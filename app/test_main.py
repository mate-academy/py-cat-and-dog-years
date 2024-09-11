from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,converted_ages",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "negative ages should be converted to zeros",
        "zero ages should be converted to zeros",
        "14/14 cat/dog ages should be converted to [0, 0] humans",
        "15/15 cat/dog ages should be converted to [1, 1] humans",
        "23/23 cat/dog ages should be converted to [1, 1] humans",
        "24/24 cat/dog ages should be converted to [2, 2] humans",
        "27/27 cat/dog ages should be converted to [2, 2] humans",
        "28/28 cat/dog ages should be converted to [3, 2] humans",
        "100/100 cat/dog ages should be converted to [21, 17] humans",
    ]
)
def test_convert_age(cat_age: int, dog_age: int, converted_ages: [int]) -> None:
    assert get_human_age(cat_age, dog_age) == converted_ages


def test_should_raise_exception_when_input_age_is_not_integer() -> None:
    with pytest.raises(TypeError):
        get_human_age("26 years", "Smith")
