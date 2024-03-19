import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_age",
    [
        (-2, -5, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (36, 44, [5, 6]),
    ]
)
def test_func_return_correct_values_for_boundary_conditions(
        cat_age: int,
        dog_age: int,
        expected_human_age: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age


def test_should_raise_error_in_wrong_input_case() -> None:
    with pytest.raises(TypeError):
        get_human_age("14", "14")
