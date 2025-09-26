import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (16, 16, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 1]),
        (25, 24, [2, 1]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (34, 34, [4, 3]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_values(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    """Test valid inputs for cat and dog ages."""
    result = get_human_age(cat_age, dog_age)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)
    assert result == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (-1, 5),
        (5, -1),
        ("10", 5),
        (5, "10"),
        (None, 5),
        (5, None),
    ],
)
def test_get_human_age_invalid(cat_age: object, dog_age: object) -> None:
    """Test invalid input types and negative ages."""
    if any(isinstance(x, int) and x < 0 for x in (cat_age, dog_age)):
        with pytest.raises(ValueError):
            get_human_age(cat_age, dog_age)
    else:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
