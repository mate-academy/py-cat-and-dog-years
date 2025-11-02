import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (33, 33, [4, 3]),
        (100, 100, [21, 17]),
    ],
)
def test_expected_values(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    """Check correct human age conversions for cats and dogs."""
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -5),
        (-3, -3),
    ],
)
def test_negative_ages(cat_age: int, dog_age: int) -> None:
    """Function should handle negative inputs without raising exceptions."""
    result = get_human_age(cat_age, dog_age)
    assert isinstance(result, list)
    assert len(result) == 2


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("10", 5),
        (None, 10),
        (8, "12"),
    ],
)
def test_invalid_string_and_none_types(
    cat_age: object, dog_age: object
) -> None:
    """Ensure string or None inputs raise TypeError."""
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


def test_float_input_does_not_raise() -> None:
    """Floats should be handled without raising exceptions."""
    result = get_human_age(7.5, 3)
    assert isinstance(result, list)
    assert len(result) == 2
