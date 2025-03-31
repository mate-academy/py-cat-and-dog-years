import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (100, 150, [21, 27]),
        (-10, -10, [0, 0]),
        (-10, -150, [0, 0]),
        (10000, 10000, [2496, 1997]),
    ],
    ids=[
        "0 cat/dog years should convert into 0 human age.",
        "14 cat/dog years should convert into 0 human age.",
        "15 cat/dog years should convert into 1 human age.",
        "23 cat/dog years should convert into 1 human age.",
        "24 cat/dog years should convert into 2 human age.",
        "27 cat/dog years should convert into 2 human age.",
        "28 cat/dog years should convert into 3/2 human age accordingly.",
        "100 cat/dog years should convert into 21/17 human age accordingly.",
        "100 cat/ 150 dog years should convert into "
        "21/27 human age accordingly.",
        "-10 cat/dog years should convert into 0 human age.",
        "-10 cat/ -150 dog years should convert into 0 human age.",
        "10000 cat/dog years should convert into "
        "2496 / 1997 human age accordingly.",
    ]
)
def test_first_15_years(cat_age: int, dog_age: int, result: list) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), "function should return appropriate value"


@pytest.mark.parametrize(
    "values,expected_error",
    [
        pytest.param(
            {"cat_age": "10", "dog_age": 10},
            TypeError,
            id="inappropriate data type!"
        ),
        pytest.param(
            {"cat_age": [10], "dog_age": [10]},
            TypeError,
            id="inappropriate data type!"
        )
    ]
)
def test_incorrect_type(values: dict, expected_error: Exception) -> None:
    with pytest.raises(expected_error):
        get_human_age(**values)
