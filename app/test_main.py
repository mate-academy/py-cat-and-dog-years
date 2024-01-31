import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (0, 0, [0, 0]),
        (-15, -24, [0, 0]),
        (12, 14, [0, 0]),
        (18, 16, [1, 1]),
        (23, 24, [1, 2]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
    ],
    ids=[
        "0 cat/dogs years should convert into 0 human age",
        "<0 cat/dogs years should convert into 0 human age",
        "<1 cat/dogs years should convert into 0 human age",
        "15 cat/dogs years should convert into 1 human age",
        "23 cat/dogs years should convert into 1 human age",
        "24 cat/dogs years should convert into 2 human age",
        "27/28 cat/dogs years should convert into 2 human age",
        "28/29 cat/dogs years should convert into 3 human age",
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: list[int]
) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected_result
