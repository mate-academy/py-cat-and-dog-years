import pytest
from typing import Any
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_ages",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (25, 25, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
        (120, 130, [26, 23]),
    ],
)
def test_get_human_age_various_scenarios(
    cat_age: int, dog_age: int, expected_human_ages: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_ages


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (23.9, 23.9, [1, 1]),
        (24.0, 24.0, [2, 2]),
    ]
)
def test_get_human_age_handles_float_values(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("20", 30),
        (20, "30"),
    ]
)
def test_get_human_age_raises_error_for_string_types(
    cat_age: Any, dog_age: Any
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
