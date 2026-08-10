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
        (14, 15, [0, 1]),
        (15, 14, [1, 0]),
        (23, 24, [1, 2]),
        (24, 23, [2, 1]),
        (27, 28, [2, 2]),
        (28, 27, [3, 2]),
    ],
)
def test_get_human_age(
    cat_age: int, dog_age: int, expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 0),
        (0, -1),
        (-1, -1),
    ],
)
def test_get_human_age_with_negative_values(
    cat_age: int, dog_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [0, 0]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        ("15", "15"),
    ],
)
def test_get_human_age_with_string_values(
    cat_age: str, dog_age: str
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
