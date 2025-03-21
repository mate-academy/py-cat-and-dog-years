import pytest
from app.main import get_human_age


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
    ],
    ids=[
        "-> negative <- numbers must return [0, 0]",
        "-> 0, 0 <- zeros mush return [0, 0]",
        "-> 14, 14 <- must return [0, 0]",
        "-> 15, 15 <- must return [1, 1]",
        "-> 23, 23 <- must return [1, 1]",
        "-> 24, 24 <- must return [2, 2]",
        "-> 27, 27 <- must return [2, 2]",
        "-> 28, 28 <- must return [3, 2]",
        "-> 100, 100 <- must return [21, 17]"
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, human_age: int) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


def test_get_human_age_is_not_int_type() -> None:
    with pytest.raises(TypeError):
        get_human_age(get_human_age("24", [20], (20), {"20": 20}))
