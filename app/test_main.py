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
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-5, -10, [0, 0]),
    ],
)
def test_get_human_age_valid_values(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("fifteen", 15),
        (15, "ten"),
        (None, 5),
        ([15], 5),
        (15, 5.5),
    ],
)
def test_get_human_age_invalid_types(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
