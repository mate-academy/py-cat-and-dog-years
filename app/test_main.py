from app.main import get_human_age
from typing import Type
import pytest


@pytest.mark.parametrize(
    "initial_cat_age,initial_dog_age,result",
    [
        pytest.param(14, 14, [0, 0], id="Test for ages less than one year"),
        pytest.param(23, 23, [1, 1], id="Test for one year"),
        pytest.param(24, 24, [2, 2], id="Test for two years"),
        pytest.param(100, 100, [21, 17], id="Test for different results"),
    ]
)
def test_should_comply_the_rules(initial_cat_age: int,
                                 initial_dog_age: int,
                                 result: list[int]) -> None:
    assert get_human_age(initial_cat_age, initial_dog_age) == result


@pytest.mark.parametrize(
    "initial_cat_age,initial_dog_age,normalization",
    [
        pytest.param(0, 0, [0, 0], id="Test for two zeros"),
        pytest.param(-23, -23, [0, 0], id="Test for two negative numbers"),
        pytest.param(123456789012345678901234567890123456789012345,
                     123456789, [30864197253086419725308641972530864197253082,
                                 24691355], id="Test for two large numbers"),
        pytest.param(15, 24, [1, 2], id="Test for edge case"),
        pytest.param(10.5, 11.2, [0, 0], id="Test for float rounding"),

    ]
)
def test_out_of_range_data(initial_cat_age: int,
                           initial_dog_age: int,
                           normalization: list[int]) -> None:
    assert get_human_age(initial_cat_age, initial_dog_age) == normalization


@pytest.mark.parametrize(
    "initial_cat_age,initial_dog_age,expected_error",
    [
        pytest.param(None, 0, TypeError, id="should raise TypeError"),
        pytest.param(5, {}, TypeError, id="should raise TypeError"),
        pytest.param("abc", 20, TypeError,
                     id="Test if TypeError is raised for string input"),

    ]
)
def test_raising_errors_correctly(initial_cat_age: int,
                                  initial_dog_age: int,
                                  expected_error: Type[Exception]) -> None:
    with pytest.raises(expected_error):
        get_human_age(initial_cat_age, initial_dog_age)
