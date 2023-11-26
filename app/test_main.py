import pytest

from app.main import get_human_age


def test_output_integer_value_not_change_previous_value() -> None:
    assert (get_human_age(cat_age=15, dog_age=15)
            != get_human_age(cat_age=30, dog_age=35))


@pytest.mark.parametrize("cat_age, dog_age, expected_result",
                         [(0, 0, [0, 0]),
                          (14, 15, [0, 1]),
                          (23, 23, [1, 1]),
                          (28, 28, [3, 2]),
                          (100, 100, [21, 17]),
                          (-1, 15, [0, 1])
                          ]
                         )
def test_correct_calculation_of_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


def test_should_raise_error_if_func_receives_not_correct_data_type() -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age=15, dog_age="one")
