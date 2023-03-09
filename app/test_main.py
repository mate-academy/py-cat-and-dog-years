import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (10, 10, [0, 0]),
        (15, 15, [1, 1]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "Check zeros",
        "10 cat and dog years return 0 human age",
        "15 cat and dog years return 1 human age",
        "28 cat and dog years return 3 and 2 human age",
        "Check large cat and dog years"
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("ten", 10),
        (10, [10]),
        (object, 10)
    ],
    ids=[
        "String in cat age should raise TypeError",
        "List in dog age should raise TypeError",
        "Object in cat age should raise TypeError"
    ]
)
def test_function_raises_error(cat_age: int, dog_age: int,) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
