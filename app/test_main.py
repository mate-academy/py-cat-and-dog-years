import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3])
    ],
    ids=[
        "should convert 0 cat and dog years to 0 human years",
        "should convert 14 cat and dog years to 0 human years",
        "should convert 15 cat and dog years to 1 human years",
        "should convert 23 cat and dog years to 1 human years",
        "should convert 24 cat and dog years to 2 human years",
        "should convert 27 cat and 28 dog years to 2 human years",
        "should convert 28 cat and 29 dog years to 3 human years",
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    actual = get_human_age(cat_age, dog_age)

    assert actual == expected
