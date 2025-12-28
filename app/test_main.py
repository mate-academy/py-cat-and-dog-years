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
    ids=[
        "both_zero",
        "both_under_first_threshold",
        "both_one",
        "both_one_under_increment",
        "both_increment_to_two",
        "both_under_second_threshold_two",
        "cat_age_3_dog_age_2",
        "cat_age_21_dog_age_17",
    ]
)
def test_get_human_age_valid(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 5),
        (3, -2),
        (-10, -10),
    ],
    ids=[
        "cat_negative",
        "dog_negative",
        "both_negative",
    ]
)
def test_get_human_age_negative_values(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("3", 5),
        (3, "5"),
        (3.5, 2),
        (None, 4),
        ([1], 2),
        (2, {"age": 3}),
    ],
    ids=[
        "cat_str",
        "dog_str",
        "cat_float",
        "cat_none",
        "cat_list",
        "dog_dict",
    ]
)
def test_get_human_age_invalid_types(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
