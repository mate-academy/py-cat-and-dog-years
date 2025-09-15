import pytest
from app.main import get_human_age


@pytest.mark.parametrize(

    "cat_age,dog_age,list_of_human_age",
    [
        (0, 0, [0, 0]),
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


def test_return_type() -> None:
    assert isinstance(get_human_age(10, 10), list)
    assert isinstance(get_human_age(10, 10)[0], int)
    assert isinstance(get_human_age(10, 10)[1], int)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (-10, 10),
        (10, -10),
        (10.5, 10),
        (10, 10.5),
    ],
    ids=[
        "cat_age as negative value",
        "dog_age as negative value",
        "cat_age as float value",
        "dog_age as float value",
    ]
)
def test_float_input_without_exception(cat_age: int,
                                       dog_age: int) -> None:
    assert get_human_age(cat_age, dog_age) == [0, 0]


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("10", 10),
        (10, "10"),
        ([30], 25),
        (30, [25]),
        ("abc", "def"),
        (None, 10),
        (10, None),
    ],
    ids=[
        "cat_age as string",
        "dog_age as string",
        "cat_age as list",
        "dog_age as list",
        "both as strings",
        "cat_age as None",
        "dog_age as None",
    ]
)
def test_invalid_input_types_raise_typeerror(cat_age: int,
                                             dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
