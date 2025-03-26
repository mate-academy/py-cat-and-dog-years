import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age: int, dog_age: int, expected: list[int]",
    [
        (0, 0, [0, 0]),  # Both ages are 0
        (15, 15, [1, 1]),  # First threshold
        (23, 23, [1, 1]),  # Below second threshold
        (24, 24, [2, 2]),  # Exactly at second threshold
        (28, 28, [3, 2]),  # Slightly over the second threshold
        (100, 100, [21, 17]),  # Large numbers
    ],
)
def test_get_human_age_standard_cases(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == expected
    ), f"Failed for cat_age={cat_age}, dog_age={dog_age}"


# Edge case: Negative numbers
@pytest.mark.parametrize(
    "cat_age: int, dog_age: int",
    [
        (-1, 10),  # Negative cat age
        (10, -1),  # Negative dog age
        (-5, -5),  # Both ages negative
    ],
)
def test_get_human_age_negative_numbers(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError, match="Age cannot be negative"):
        get_human_age(cat_age, dog_age)


# Edge case: Non-integer inputs
@pytest.mark.parametrize(
    "cat_age: object, dog_age: object",
    [
        ("15", 10),  # Cat age as string
        (15, "10"),  # Dog age as string
        ("fifteen", "ten"),  # Both as strings
        (15.5, 10),  # Cat age as a float
        (15, 10.5),  # Dog age as a float
    ],
)
def test_get_human_age_invalid_types(cat_age: object, dog_age: object) -> None:
    with pytest.raises(TypeError, match="Age must be an integer"):
        get_human_age(cat_age, dog_age)


# Edge case: Large numbers
def test_get_human_age_large_numbers() -> None:
    assert get_human_age(10**6, 10**6) == [
        250001,
        200001,
    ], "Failed for large input values"


# Edge case: Integer transition
@pytest.mark.parametrize(
    "cat_age: int, dog_age: int, expected: list[int]",
    [
        (27, 27, [2, 2]),  # Just below a transition point
        (28, 28, [3, 2]),  # At a transition point
        (29, 29, [3, 3]),  # Just after a transition point
    ],
)
def test_get_human_age_integer_transition(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == expected
    ), f"Failed for transition cat_age={cat_age}, dog_age={dog_age}"
