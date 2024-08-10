import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (-2, -3, [0, 0]),
        (-2, 3, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "both values are zero",
        "both values are negative",
        "one value is negative",
        "one animals year less than human year",
        "first human year",
        "two human years",
        "with big numbers"
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("two", -1),
        ("ten", "five"),
        (None, None),
    ],
    ids=[
        "string and negative number",
        "two strings",
        "two None type"
    ],
)
def test_get_human_age_invalid_input(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
