import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "cat-1_dog-1 -> 0_0",
        "cat0_dog0 -> 0_0",
        "cat14_dog14 -> 0_0",
        "cat15_dog15 -> 1_1",
        "cat23_dog23 -> 1_1",
        "cat24_dog24 -> 2_2",
        "cat27_dog27 -> 2_2",
        "cat28_dog28 -> 3_2",
        "cat100_dog100 -> 21_17",
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("cat", "dog"),
        (None, None),
        ([], {}),
        (10, "dog"),
        ("cat", 10),
    ],
    ids=[
        "strings",
        "none_values",
        "wrong_collections",
        "dog_invalid",
        "cat_invalid",
    ]
)
def test_get_human_age_invalid_types(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
