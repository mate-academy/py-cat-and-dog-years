from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="test_should_return_zero_when_input_is_zero"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="test_should_return_zero_when_age_is_less_than_15"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="test_should_return_correct_result_after_15_years"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="test_should_return_correct_"
               "result_between_15_and_next_9_years"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="test_should_return_correct_result_between_next_9_years"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="test_should_return_"
               "correct_result_between_9_and_next_4_cat_years"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="test_should_return_correct_cat_next_4_years"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="test_should_return_correct_"
               "result_over_a_long_period_of_time"
        )
    ]
)
def test_correct_human_year_result(cat_age: int,
                                   dog_age: int,
                                   result: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        pytest.param(
            -1,
            -5,
            KeyError,
            id="test_should_raise_error_when_incorrect_value_given"
        ),
        pytest.param(
            1001,
            1001,
            ValueError,
            id="test_should_raise_error_for_large_numbers"
        ),
        pytest.param(
            "two",
            3,
            TypeError,
            id="test_should_raise_error_for_incorrect_type_cat_age"
        ),
        pytest.param(
            2,
            "three",
            TypeError,
            id="test_should_raise_error_for_incorrect_type_dog_age"
        ),
    ]
)
def test_correct_error_raises(cat_age: int,
                              dog_age: int,
                              expected_error: Exception) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
