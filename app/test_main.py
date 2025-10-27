import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_values",
    [
        pytest.param(
            14, 14,
            [0, 0],
            id="convert cat and dog age to human correctly"
        ),

        pytest.param(
            -10, -1,
            [0, 0],
            id="should handle negative input"
        ),
        pytest.param(
            0, 0,
            [0, 0],
            id="should handle zero input"
        ),
        pytest.param(
            2000, 99999,
            [496, 19997],
            id="should handle large input"
        ),
    ]
)
def test_function_works_correctly(
        cat_age: int,
        dog_age: int,
        expected_values: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_values


def test_output_differs_for_different_values() -> None:
    assert get_human_age(15, 15) != get_human_age(30, 30)


def test_raises_type_error_for_invalid_input() -> None:
    with pytest.raises(TypeError):
        get_human_age("19", [1])
