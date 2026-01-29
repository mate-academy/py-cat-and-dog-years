import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "age,expected",
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (27, 2),
        (28, 3),
        (29, 3),
        (100, 21)
    ],
)
def test_cat_human_age(age: int , expected: int) -> None:
    assert get_human_age(age, age)[0] == expected


@pytest.mark.parametrize(
    "age,expected",
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (28, 2),
        (29, 3),
        (33, 3),
        (34, 4),
        (100, 17),
    ],
)
def test_dog_human_age(age: int, expected: int) -> None:
    assert get_human_age(age, age)[1] == expected

@pytest.mark.parametrize(
        "age",
        [
            "10",
             10.5,
             None,
             [1],
             {1}
        ]
)
def test_cat_input_type(age) -> None:
    with pytest.raises(TypeError):
        get_human_age(age, 10)

@pytest.mark.parametrize(
        "age",
        [
            "10",
             10.5,
             None,
             [1],
             {1}
        ]
)
def test_dog_input_type(age) -> None:
    with pytest.raises(TypeError):
        get_human_age(10, age)

@pytest.mark.parametrize(
        "negative_value",
        [
            -1,
            -20,
            -27,
            -44,
            -100
        ]
)
def test_cat_negative_value(negative_value) -> None:
    with pytest.raises(ValueError):
        get_human_age(negative_value, 10)

@pytest.mark.parametrize(
        "negative_value",
        [
            -1,
            -20,
            -27,
            -44,
            -100
        ]
)
def test_dog_negative_value(negative_value) -> None:
    with pytest.raises(ValueError):
        get_human_age(10, negative_value)

