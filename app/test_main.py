import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (5, 5, 0),
        (15, 15, 1),
        (23, 23, 1),
        (24, 24, 2),
        (27, 28, 2),
        (28, 29, 3),
    ],
    ids=[
        "5 cat/dog years should convert into 0 human age.",
        "15 cat/dog years should convert into 1 human age.",
        "23 cat/dog years should convert into 1 human age.",
        "24 cat/dog years should convert into 2 human age.",
        "27/28 cat/dog years should convert into 2 human age.",
        "28/29 cat/dog years should convert into 3 human age.",
    ]
)
def test_check_convert_correctly(cat_age: int, dog_age: int, result: int):
    assert get_human_age(cat_age, dog_age) == result
