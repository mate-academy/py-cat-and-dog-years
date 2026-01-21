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
        "before_first_year",
        "exactly_one_year",
        "before_second_year",
        "exactly_two_years",
        "before_third_year",
        "cat_third_year_dog_second",
        "senior_ages"
    ]
)
def test_get_human_age_examples(
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
        (-10, -10),
    ],
    ids=["negative_cat", "negative_dog", "both_negative"]
)
def test_get_human_age_with_negative_numbers(
    cat_age: int,
    dog_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [0, 0]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("10", 10),
        (10, "10"),
        ([10], 10),
    ],
    ids=["string_cat", "string_dog", "list_input"]
)
def test_get_human_age_raises_type_error(
    cat_age: any,
    dog_age: any
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
