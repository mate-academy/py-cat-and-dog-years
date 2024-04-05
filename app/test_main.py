import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-5, -5, [0, 0]),
        (3, 3, [0, 0]),
        (20, 10, [1, 0]),
    ],
    ids=[
        "both 0 years returns [0, 0]",
        "both 14 years returns [0, 0]",
        "both 15 years returns [1, 1]",
        "both 23 years returns [1, 1]",
        "both 24 years returns [2, 2]",
        "both 27 years returns [2, 2]",
        "cat 28 dog 28 returns [3, 2]",
        "cat 100 dog 100 returns [21, 17]",
        "cat negative 5 dog negative 5 returns [0, 0]",
        "cat 3 dog 3 returns [0, 0]",
        "cat 20 dog 10 returns [1, 0]",
    ],
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ["cat", 0],
        None,
        [0, 0],
        {0, 0}
    ]
)
def test_get_human_age_errors(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
