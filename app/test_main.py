import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        (-1, -15, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       human_age: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, error",
    [
        ("1", 2, TypeError),
        (3, None, TypeError),
    ]
)
def test_ages_need_to_be_int(cat_age: int,
                             dog_age: int,
                             error: type(TypeError)) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)
