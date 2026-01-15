from app.main import get_human_age
import pytest



@pytest.mark.parametrize(
    "cat_age,dog_age,in_human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17])
    ],
    ids=[
            "0 cat/dog years should convert into 0 human age.",
            "14 cat/dog years should convert into 0 human age.",
            "15 cat/dog years should convert into 1 human age.",
            "23 cat/dog years should convert into 1 human age.",
            "24 cat/dog years should convert into 2 human age.",
            "27/28 cat/dog years should convert into 2 human age.",
            "28/29 cat/dog years should convert into 3 human age.",
            "100 cat/dog years should convert into 21/17 human age."
        ]
)
def test_get_human_age(cat_age, dog_age, in_human_age):
    assert get_human_age(cat_age, dog_age) == in_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        (-1, -1, ValueError),
        (151, 1, ValueError),
        (0.4, 0.2, TypeError)
    ],
    ids=[
            "-1/-1 cat/dog years should raise ValueError.",
            "151/1 cat/dog years should raise ValueError.",
            "0.4 cat/dog years should raise TypeError."
    ]
)
def test_get_human_age_errors(cat_age, dog_age, expected_error):
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
