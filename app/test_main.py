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
        "zero_age",
        "before_first_threshold",
        "at_first_threshold",
        "before_second_threshold",
        "at_second_threshold",
        "before_extra_step",
        "after_cat_extra_step",
        "large_values",
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 5),
        (5, -1),
        (-10, -10),
    ],
    ids=[
        "negative_cat",
        "negative_dog",
        "both_negative",
    ],
)
def test_negative_age_raises_value_error(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("10", 5),     # cat as string
        (5, "10"),     # dog as string
        (None, 5),     # cat as None
        (5, None),     # dog as None
        ([], 5),       # cat as list
        (5, {}),       # dog as dict
    ],
    ids=[
        "cat_string",
        "dog_string",
        "cat_none",
        "dog_none",
        "cat_list",
        "dog_dict",
    ],
)
def test_incorrect_type_raises_type_error(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
