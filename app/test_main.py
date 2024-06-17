import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, cat_result, dog_result",
    [
        (-15, -14, 0, 0),
        (0, 0, 0, 0),
        (14, 14, 0, 0),
        (15, 15, 1, 1),
        (23, 23, 1, 1),
        (24, 24, 2, 2),
        (27, 28, 2, 2),
        (28, 29, 3, 3),
        (100, 100, 21, 17),
    ],
    ids=[

        "negative value of cat/dog years should return 0 human age.",
        "0 cat/dog years should convert into 0 human age.",
        "14 cat/dog years should convert into 0 human age.",
        "15 cat/dog years should convert into 1 human age.",
        "23 cat/dog years should convert into 1 human age.",
        "24 cat/dog years should convert into 2 human age.",
        "27/28 cat/dog years should convert into 2 human age.",
        "28/29 cat/dog years should convert into 3 human age.",
        "100 cat/dog years should convert into 21/17 human age.",
    ]
)
def test_ages(
        cat_age: int,
        dog_age: int,
        cat_result: int,
        dog_result: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [cat_result, dog_result]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("", ""),
        (None, None)
    ],
    ids=[
        "Not integer value should raise TypeError",
        "None value should raise TypeError"
    ]
)
def test_errors(cat_age: any, dog_age: any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
