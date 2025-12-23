import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
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
        "should convert negative years into zero",
        "should convert zero years into zero",
        "should convert 14 cat/dog years into zero",
        "should convert 15 cat/dog years into 1 human age",
        "should convert 23 cat/dog years into 1 human age",
        "should convert 24 cat/dog years into 2 human age",
        "should convert 27/28 cat/dog years into 2 human age",
        "should convert 28/29 cat/dog years into 3 human age",
        "should convert large value of cat/dog age to human years as expected",
    ]
)
def test_age_convertion(cat_age: int, dog_age: int, result: int) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_should_raise_error_when_animal_age_is_not_number() -> None:
    with pytest.raises(TypeError):
        get_human_age("hi", [23, 17])
