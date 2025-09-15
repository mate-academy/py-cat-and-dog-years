import pytest
from app.main import get_human_age


@pytest.mark.parametrize(

    "cat_age,dog_age,list_of_human_age",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        pytest.param(-30, 15, [0, 1], id="negative value return 0"),
        pytest.param(10.0, 15, [0, 1], id="float value return 0")
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       list_of_human_age: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == list_of_human_age


def test_get_human_age_negative_value() -> None:
    assert get_human_age(-30, 15) == [0, 1]


def test_get_human_age_float_value() -> None:
    assert get_human_age(10.0, 15) == [0, 1]


def test_value_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("10", 10)
        get_human_age([30], "25")
        get_human_age(10, 10.5)
        get_human_age(100, {})
