from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_age_cat,expected_age_dog",
    [
        (15, 15, 1, 1),
        (14, 14, 0, 0),
        (23, 23, 1, 1),
        (24, 24, 2, 2),
        (28, 28, 3, 2),
        (27, 27, 2, 2),
        (100, 100, 21, 17),
        (0, 0, 0, 0),
        (39, 51, 5, 7)
    ],
    ids=[
        "15/15 cat/dog years should convert into 1/1 human age.",
        "14/14 cat/dog years should convert into 0/0 human age.",
        "23/23 cat/dog years should convert into 1/1 human age.",
        "24/24 cat/dog years should convert into 2/2 human age.",
        "28/28 cat/dog years should convert into 3/2 human age.",
        "27/27 cat/dog years should convert into 2/2 human age.",
        "100/100 cat/dog years should convert into 21/17 human age.",
        "0/0 cat/dog years should convert into 0/0 human age.",
        "39/51 cat/dog years should convert into 5/7 human age.",
    ]
)
def test_check_get_human_age(cat_age, dog_age, expected_age_cat, expected_age_dog):

    assert get_human_age(cat_age, dog_age) == [expected_age_cat, expected_age_dog]
