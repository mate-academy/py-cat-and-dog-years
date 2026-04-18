import pytest
from typing import Any, Type

from app.main import get_human_age, NegativeAgeError, LargeAgeError


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(0, 0, [0, 0], id="zero_zero"),
        pytest.param(14, 14, [0, 0], id="before_first_step"),
        pytest.param(15, 15, [1, 1], id="first_step"),
        pytest.param(23, 23, [1, 1], id="before_second_step"),
        pytest.param(24, 24, [2, 2], id="second_step"),
        pytest.param(27, 27, [2, 2], id="before_third_step"),
        pytest.param(28, 28, [3, 2], id="third_step_transition"),
        pytest.param(29, 29, [3, 3], id="after_third_step"),
    ]
)
def test_different_values(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,name_of_exception",
    [
        pytest.param(-5, 15, NegativeAgeError, id="negative_age_Cat"),
        pytest.param(0, -15, NegativeAgeError, id="negative_age_Dog"),
        pytest.param(16666, 3, LargeAgeError, id="large_age_Cat"),
        pytest.param(7, 48, LargeAgeError, id="large_age_Dog"),
        pytest.param(None, 3, TypeError, id="Cat_None"),
        pytest.param(4, "4", TypeError, id="Dog_str"),
        pytest.param([12], 3, TypeError, id="Cat_list"),
        pytest.param(4, 4.0, TypeError, id="Dog_float"),
        pytest.param(False, 3, TypeError, id="Cat_bool"),
        pytest.param(4, {"dog_age": 12}, TypeError, id="Dog_dict"),
    ]
)
def test_incorrect_values(
    cat_age: Any,
    dog_age: Any,
    name_of_exception: Type[Exception]
) -> None:
    with pytest.raises(name_of_exception):
        get_human_age(cat_age, dog_age)
