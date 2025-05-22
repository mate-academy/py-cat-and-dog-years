import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_cat, expected_dog",
    [
        (0, 0, 0, 0),
        (14, 14, 0, 0),
        (15, 15, 1, 1),
        (23, 23, 1, 1),
        (24, 24, 2, 2),
        (27, 27, 2, 2),
        (28, 28, 3, 2),
        (100, 100, 21, 17)
    ],
    ids=[
        "0 cat/dog years should convert into 0 human age.",
        "14 cat/dog years should convert into 0 human age.",
        "15 cat/dog years should convert into 1 human age.",
        "23 cat/dog years should convert into 1 human age.",
        "24 cat/dog years should convert into 2 human age.",
        "27 cat/dog years should convert into 2 human age.",
        "28 cat/dog years should convert into 3/2 human age.",
        "100 cat/dog years should convert into 21/17 human age.",
    ]
)
def test_convert_to_human_age(
        cat_age: int,
        dog_age: int,
        expected_cat: int,
        expected_dog: int) -> None:
    result = get_human_age(cat_age, dog_age)
    assert (result == [expected_cat, expected_dog]), \
        f"Expected [{expected_cat}, {expected_dog}], but got {result}"
