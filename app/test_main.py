from typing import Any

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(0, 0, [0, 0], id="both_zero"),
        pytest.param(14, 14, [0, 0], id="below_first_boundary"),
        pytest.param(15, 15, [1, 1], id="first_boundary"),
        pytest.param(23, 23, [1, 1], id="below_second_boundary"),
        pytest.param(24, 24, [2, 2], id="second_boundary"),
        pytest.param(27, 27, [2, 2], id="below_third_boundary"),
        pytest.param(28, 28, [3, 2], id="third_boundary_cat_only"),
        pytest.param(29, 29, [3, 3], id="third_boundary_dog"),
        pytest.param(100, 100, [21, 17], id="large_values"),
        pytest.param(1000, 1000, [246, 197], id="very_large_values"),
    ],
)
def test_get_human_age_valid_values(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    """Checks correct age conversion for various valid input ranges."""
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_prev, cat_next",
    [
        pytest.param(14, 15, id="cat_boundary_0_to_1"),
        pytest.param(23, 24, id="cat_boundary_1_to_2"),
        pytest.param(27, 28, id="cat_boundary_2_to_3"),
    ],
)
def test_cat_output_changes_on_boundaries(
    cat_prev: int,
    cat_next: int,
) -> None:
    """Ensures cat age changes exactly at documented boundary points."""
    prev_val = get_human_age(cat_prev, 0)[0]
    next_val = get_human_age(cat_next, 0)[0]
    assert prev_val != next_val


@pytest.mark.parametrize(
    "dog_prev, dog_next",
    [
        pytest.param(14, 15, id="dog_boundary_0_to_1"),
        pytest.param(23, 24, id="dog_boundary_1_to_2"),
        pytest.param(28, 29, id="dog_boundary_2_to_3"),
    ],
)
def test_dog_output_changes_on_boundaries(
    dog_prev: int,
    dog_next: int,
) -> None:
    """Ensures dog age changes exactly at documented boundary points."""
    prev_val = get_human_age(0, dog_prev)[1]
    next_val = get_human_age(0, dog_next)[1]
    assert prev_val != next_val


def test_get_human_age_negative_values() -> None:
    """
    Checks behavior for out-of-normal-range negative ages.
    According to current implementation they are treated as 0.
    """
    assert get_human_age(-1, -5) == [0, 0]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param("15", 10, id="cat_as_string"),
        pytest.param(15, "10", id="dog_as_string"),
        pytest.param("15", "10", id="both_as_string"),
    ],
)
def test_get_human_age_incorrect_types(
    cat_age: Any,
    dog_age: Any,
) -> None:
    """
    Ensures that passing incorrect data types leads to TypeError.
    """
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
