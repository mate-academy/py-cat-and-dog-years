import pytest
from app.main import get_human_age

@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (14, 14, [0, 0]),  # 14 cat years should convert into 0 human age, 14 dog years should convert into 0 human age.
        (15, 15, [1, 1]),  # 15 cat years should convert into 1 human age, 15 dog years should convert into 1 human age.
        (23, 23, [1, 1]),  # 23 cat years should convert into 1 human age, 23 dog years should convert into 1 human age.
        (24, 24, [2, 2]),  # 24 cat years should convert into 2 human age, 24 dog years should convert into 2 human age.
        (27, 28, [2, 2]),  # 27 cat years should convert into 2 human age, 28 dog years should convert into 2 human age.
        (28, 29, [3, 3]),  # 28 cat years should convert into 3 human age, 29 dog years should convert into 3 human age.
    ],
    ids=[
        "14 cat/dog years should convert into 0 human age.",
        "15 cat/dog years should convert into 1 human age.",
        "23 cat/dog years should convert into 1 human age.",
        "24 cat/dog years should convert into 2 human age.",
        "27/28 cat/dog years should convert into 2 human age.",
        "28/29 cat/dog years should convert into 3 human age.",
    ]
)
def test_cat_and_dog_into_human_age(cat_age: int, dog_age: int, expected_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
