import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-2, -2, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age_correct_input(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,error_msg",
    [
        ("10", "10", TypeError),
        (None, None, TypeError),
        ({}, {}, TypeError)
    ]
)
def test_type_err_exceptions(
        cat_age: int,
        dog_age: int,
        error_msg: type[Exception]
) -> None:
    with pytest.raises(error_msg):
        get_human_age(cat_age, dog_age)
