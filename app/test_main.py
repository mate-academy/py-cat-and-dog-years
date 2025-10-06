import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (24, 24, [2, 2]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_example_assertions(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-1, -1, [0, 0]),
        (-10, -10, [0, 0]),
        (-1, 24, [0, 2]),
        (24, -1, [2, 0]),
    ],
)
def test_get_human_negative_values(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    """Negative values should be treated as zero-equivalent."""
    assert get_human_age(cat_age, dog_age) == expected


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
    ],
)
def test_get_human_basic(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("2", 3),
        (3, "2"),
        (None, 5),
        (5, None),
    ],
)
def test_get_human_invalid_types(cat_age: int, dog_age: int) -> None:
    """Invalid input types should raise TypeError."""
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (23, 0, [1, 0]),
        (24, 0, [2, 0]),
        (27, 0, [2, 0]),
        (28, 0, [3, 0]),
    ],
)
def test_get_human_cat_limits(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 23, [0, 1]),
        (0, 24, [0, 2]),
        (0, 27, [0, 2]),
    ],
)
def test_get_human_dog_limits(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected


def test_get_human_returns_list() -> None:
    """Check return type and length."""
    result = get_human_age(10, 10)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)
