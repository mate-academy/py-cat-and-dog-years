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
    ]
)
def test_get_human_age_valid(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 5),
        (5, -1),
        ("15", 5),
        (5, "10"),
        (1.5, 5),
        (5, 2.7),
        (1000, 1000),
    ]
)
def test_get_human_age_invalid(cat_age: object, dog_age: object) -> None:
    with pytest.raises((TypeError, ValueError)):
        get_human_age(cat_age, dog_age)
