import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "-1, -1 should return [0, 0]",
        "0, 0, should return [0, 0]",
        "15, 15, should return [1, 1]",
        "23, 23, should return [1, 1]",
        "24, 24, should return [2, 2]",
        "27, 27, should return [2, 2]",
        "28, 28, should return [3, 2]",
        "100, 100, should return [21, 17]"
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, human_age: int) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize("cat_age, dog_age, human_age", [
    ("1", 1, TypeError),
    (1, "1", TypeError),
    ("1", "1", TypeError),
])
def test_get_human_age_errors(
        cat_age: int,
        dog_age: int,
        human_age: int
) -> None:
    with pytest.raises(human_age):
        get_human_age(cat_age, dog_age)
