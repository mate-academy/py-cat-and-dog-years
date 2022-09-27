from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (
            28,
            28,
            [3, 2]
        ),
        (
            0,
            0,
            [0, 0]
        ),
        (
            15,
            15,
            [1, 1]
        ),
        (
            100,
            100,
            [21, 17]
        )
    ]
)
def test_function_correct_working(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected


def test_should_raise_error_when_arguments_not_int():
    with pytest.raises(TypeError):
        get_human_age("one", [2, 3, 4])


def test_should_raise_error_when_not_2_arguments_passed_to_function():
    with pytest.raises(TypeError):
        get_human_age(24)
