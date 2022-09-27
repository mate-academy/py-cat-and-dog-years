from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="When human years less than 15 function should return 0 year"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="When human years less than 15 function should return 0 year"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="When human years between 15 and 24 "
               "function should return 1 year"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="When human years between 15 and 24 "
               "function should return 1 year"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="When human years between 25 and 28 function should return 2"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="When human years is 28 function should return "
               "3 cats and 2 dogs years"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="When human years is 100 function should return "
               "21 cats and 17 dogs years"
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
