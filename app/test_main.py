import pytest
from app.main import get_human_age


# write your code here

@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ], ids=[
        "If cat age or dog is negative - should return [0, 0]",
        "Cat age is 0, dog age is 0 - should return [0, 0]",
        "Cat age is 14, dog age is 14 - should return [0, 0]",
        "Cat age is 15, dog age is 15 - should return [1, 1]",
        "Cat age is 23, dog age is 23 - should return [1, 1]",
        "Cat age is 24, dog age is 24 - should return [2, 2]",
        "Cat age is 27, dog age is 27 - should return [2, 2]",
        "Cat age is 28, dog age is 28 - should return [3, 2]",
        "Cat age is 100, dog age is 100 - should return [21, 17]"
    ]
)
def test_human_age_is_correct(
        cat_age: int,
        dog_age: int,
        human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


def test_incorrect_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("one", "two")

