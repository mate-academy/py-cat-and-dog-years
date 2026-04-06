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
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "zero_ages",
        "below_15",
        "exactly_15",
        "between_15_and_24",
        "exactly_24",
        "cat_dog_mid_range",
        "cat_extra_growth",
        "dog_boundary_29",
        "large_numbers",
    ],
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("10", 10),
        (10, "10"),
        (None, 10),
        (10, None),
        ([], 10),
        (10, {}),
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
def test_get_human_age_type_error(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -1),
        (-5, -5),
        (-100, 0),
        (0, -100),
    ],
    ids=[
        "negative_cat",
        "negative_dog",
        "both_negative",
        "large_negative_cat",
        "large_negative_dog",
    ],
)
def test_get_human_age_value_error(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)
