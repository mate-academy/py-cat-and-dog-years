import pytest
from app.main import get_human_age


def test_check_output_value_not_equal_previous_value() -> None:
    assert (get_human_age(cat_age=23, dog_age=23)
            != get_human_age(cat_age=24, dog_age=24))


@pytest.mark.parametrize("cat_age, dog_age, expected_result", [
    (0, 16, [0, 1]),
    (27, 28, [2, 2]),
    (28, 28, [3, 2]),
    (100, 150, [21, 27])
])
def test_check_data_minus_type_age_value(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
