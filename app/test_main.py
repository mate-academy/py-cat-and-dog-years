from app.main import get_human_age

import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, result, test_id",
    [
        (-14, -14, [0, 0],
         "Negative values should return zeros"),
        (0, 0, [0, 0],
         "Zero values should return zeros"),
        (14, 14, [0, 0],
         "Value of ages are less than 15"),
        (15, 15, [1, 1],
         "15 should return 1 year per value"),
        (24, 24, [2, 2],
         "24 should return 2 year per value"),
        (28, 28, [3, 2],
         "28 should return 3 for cat and 2 for dog"),
        (100, 100, [21, 17],
         "100 should return 21 for cat and 17 for dog"),
        (1000, 1000, [246, 197],
         "1000 should return very large results: 246 and 197")
    ],
)
def test_errors_for_type_values(
        cat_age: int,
        dog_age: int,
        result: list[int],
        test_id: str
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, error",
    [
        ("15", 15, TypeError),
        (15, "15", TypeError),
    ],
    ids=[
        "cat_age should be int",
        "dog_age should be int",
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, error: TypeError) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
