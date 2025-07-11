from app.main import get_human_age

import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_cat, excepted_dog",
    [
        (0, 0, 0, 0),
        (14, 14, 0, 0),
        (15, 15, 1, 1),
        (23, 23, 1, 1),
        (24, 24, 2, 2),
        (27, 28, 2, 2),
        (28, 29, 3, 3),
        (-1, -1, 0, 0),
    ],
    ids=[
        "0 cat/dog years should convert into 0 human age.",
        "14 cat/dog years should convert into 0 human age.",
        "15 cat/dog years should convert into 1 human age.",
        "23 cat/dog years should convert into 1 human age.",
        "24 cat/dog years should convert into 2 human age.",
        "27/28 cat/dog years should convert into 2 human age.",
        "28/29 cat/dog years should convert into 3 human age.",
        "-1 cat/dog years should convert into 0 human age.",
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_cat: int,
        excepted_dog: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [expected_cat, excepted_dog]


@pytest.mark.parametrize(
    "cat_age, dog_age, excepted",
    [
        ("adfa", "adfa", TypeError),
        ("dsfsd", 23, TypeError),
        (12, "df", TypeError)
    ]
)
def test_type_error_in_get_human_age(
        cat_age: int,
        dog_age: int,
        excepted: TypeError
) -> None:
    with pytest.raises(excepted):
        get_human_age(cat_age, dog_age)
