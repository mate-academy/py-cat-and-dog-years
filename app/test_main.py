import pytest

from app.main import get_human_age


# write your code here
@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-1, 1, [0, 0]),
        (1, -1, [0, 0]),
        (-1, -1, [0, 0])
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        human_age: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("1", 1),
        (1, "1"),
        ("1", "1")
    ]
)
def test_get_human_age_raises_exception(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
