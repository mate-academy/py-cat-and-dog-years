import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (16, 10, [1, 0]),
        (15, 0, [1, 0]),
        (0, 15, [0, 1]),
    ],
    ids=[
        "both_0",
        "both_14",
        "both_15",
        "both_28",
        "both_100",
        "cat_16_dog_10",
        "cat_15_dog_0",
        "cat_0_dog_15",
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("very old cat", 10),
        (15, "the same age as my son"),
        (None, 10),
        ([1, 2], 10),
    ],
    ids=[
        "cat_age_str",
        "dog_age_str",
        "cat_age_none",
        "dog_age_list",
    ]
)
def test_get_human_age_invalid_types(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
