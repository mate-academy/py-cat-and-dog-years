import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 14, [1, 0]),
        (14, 15, [0, 1]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 23, [2, 1]),
        (23, 24, [1, 2]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        (15.5, 15),
        (15, 15.5),
        (None, 15),
        (15, None),
        (-1, 15),
        (15, -1),
        (-5, -5),
    ]
)
def test_get_human_age_raises_exception_on_invalid_types(
    cat_age: int, dog_age: int
) -> None:
    with pytest.raises((TypeError, ValueError)):
        get_human_age(cat_age, dog_age)
