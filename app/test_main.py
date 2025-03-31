import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (-1, -1, [0, 0]),
        (500, 600, [121, 117]),

    ],
    ids=[
        "when ages are both zeros, should return both zeros",
        "when ages are both under 15, should return both zeros",
        "when ages are both equal 15, should return both 1",
        "when ages are both under 24, should return both 1",
        "when ages are both equal 24, should return both 2",
        "when ages are both under 28, should return both 2",
        "after ages are equal or bigger than 28, should return different age",
        "if input ages are negative, should return both zeros",
        "if input ages are too big for real life, should return result"
    ]
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    result: list[int, int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,error",
    [
        ("1", 1, TypeError),
        (1, "1", TypeError),
    ],
    ids=[
        "if cat age is string should return `TypeError`",
        "if dog age is string should return `TypeError`",
    ]
)
def test_get_human_age_error(
    cat_age: int,
    dog_age: int,
    error: Exception
) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)
