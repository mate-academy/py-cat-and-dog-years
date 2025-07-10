import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 9, [0, 0]),
        (15, 9, [1, 0]),
        (23, 14, [1, 0]),
        (24, 14, [2, 0]),
        (24, 15, [2, 1]),
        (24, 25, [2, 2]),
        (65, 79, [12, 13]),
    ],
    ids=[
        "0 cat/dog years should convert into 0 human age.",
        "14/9 cat/dog years should convert into 0 human age.",
        "15/9 cat/dog years should convert into 1/0 human age.",
        "23/14 cat/dog years should convert into 1/0 human age.",
        "24/14 cat/dog years should convert into 2/0 human age.",
        "24/15 cat/dog years should convert into 2/1 human age.",
        "24/25 cat/dog years should convert into 2/2 human age.",
        "65/79 cat/dog years should convert into 12/13 human age.",
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected
