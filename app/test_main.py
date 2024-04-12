import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (0, 0, [0, 0]),
        (-1, -1, [0, 0]),
    ],
    ids=[
        "14 cat/dog years should convert into 0 human age.",
        "15 cat/dog years should convert into 1 human age.",
        "23 cat/dog years should convert into 1 human age.",
        "24 cat/dog years should convert into 2 human age.",
        "27/28 cat/dog years should convert into 2 human age.",
        "28/29 cat/dog years should convert into 3 human age.",
        "0/0 cat/dog years should return 0 human age.",
        "-1/-1 cat/dog years should return 0 human age."
    ]
)
def test_return_correct_output(cat_age, dog_age, result) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        ("1", "1", TypeError),
        ({}, {}, TypeError)
    ]
)
def test_raising_errors_correctly(cat_age, dog_age, expected_error) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)

