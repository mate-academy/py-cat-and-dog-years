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
    ],

    ids=[
        "zero years",
        "before_year_1",
        "first human year",
        "before_year_2",
        "two human years",
        "cat extra year",
        "old animals"
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
        ("10", 10),
        (10, "10"),
        (None, 5),
    ],
    ids=[
        "invalid cat age",
        "invalid dog age",
        "empty cat age"
    ]
)
def test_get_human_age_invalid_type(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [

        (-1, 10),
        (10, -1),
        (-10, -10),
    ],
    ids=[
        "negative_cat_age",
        "negative_dog_age",
        "both_negative"
    ]
)
def test_get_human_age_invalid_range(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)
