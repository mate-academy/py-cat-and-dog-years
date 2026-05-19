import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [   (1, 0, [0, 0]),
        (-1, 0, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (1000, 1000, [246, 197])
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected

@pytest.mark.parametrize(
    "invalid_cat, invalid_dog",
    [
        (None, 10),
        ("cat", 5),
        (20, "dog"),
        (None, None),
        ([1, 2], 5),
    ]
)
def test_get_human_age_invalid_types(invalid_cat, invalid_dog):
    with pytest.raises(TypeError):
        get_human_age(invalid_cat, invalid_dog)
