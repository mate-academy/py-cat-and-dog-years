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
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_examples(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    """Test the given example cases."""
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (16, 10),
        (30, 25),
        (45, 40),
        (60, 55),
        (90, 90),
    ],
)
def test_get_human_age_increases_with_age(
    cat_age: int,
    dog_age: int,
) -> None:
    """Ensure human age never decreases as animal ages increase."""
    prev = get_human_age(max(0, cat_age - 1), max(0, dog_age - 1))
    current = get_human_age(cat_age, dog_age)
    assert current[0] >= prev[0]
    assert current[1] >= prev[1]


def test_get_human_age_output_structure() -> None:
    """Ensure function returns a list of two integers."""
    result = get_human_age(50, 70)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -5),
        (-10, -20),
    ],
)
def test_negative_ages(cat_age: int, dog_age: int) -> None:
    """Ensure negative ages return [0, 0]."""
    result = get_human_age(cat_age, dog_age)
    assert result == [0, 0]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("ten", 5),
        (5, "three"),
        (5.5, 10),
        (10, 7.3),
        (None, 5),
    ],
)
def test_invalid_input_types(
    cat_age: object,
    dog_age: object,
) -> None:
    """Ensure invalid input types raise TypeError."""
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
