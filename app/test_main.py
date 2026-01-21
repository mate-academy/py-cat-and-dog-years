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
        (28, 27, [3, 2]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_valid(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 0),
        (0, -5),
        (-10, -20),
    ],
)
def test_get_human_age_negative(cat_age: int, dog_age: int) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == [0, 0] or all(isinstance(x, int) for x in result)


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (3.5, 10, [0, 0]),
        (10, 2.7, [0, 0]),
        (15.0, 15.0, [1, 1]),
        (23.9, 24.1, [1, 2]),
    ],
)
def test_get_human_age_floats(
    cat_age: float, dog_age: float, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("ten", 5),
        (5, "dog"),
        (None, 5),
    ],
)
def test_get_human_age_invalid_types(cat_age: object, dog_age: object) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
