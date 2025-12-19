import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_human_age",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 29, [3, 3]),
        (32, 34, [4, 4]),
        (56, 64, [10, 10]),
        (100, 100, [21, 17])
    ],
    ids=[
        "-1 cat/dog age should convert into 0 human age.",
        "0 cat/dog age should convert into 0 human age.",
        "14 cat/dog age should convert into 0 human age.",
        "15 cat/dog age should convert into 1 human age.",
        "23 cat/dog age should convert into 1 human age.",
        "24 cat/dog age should convert into 2 human age.",
        "27 cat/dog age should convert into 2 human age.",
        "28/29 cat/dog age should convert into 3 human age.",
        "32/34 cat/dog age should convert into 4 human age.",
        "56/64 cat/dog age should convert into 10 human age.",
        "100 cat/dog age should convert into 21/17 human age.",
    ]
)
def test_get_human_age_should_return_correct_result(
        cat_age: int,
        dog_age: int,
        expected_human_age: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age


def test_get_human_age_should_raise_correct_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("3", [4])
