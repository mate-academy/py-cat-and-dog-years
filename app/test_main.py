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
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
        (10000, 10000, [2496, 1997]),
        (1999999, 1999999, [499995, 399997]),
        (-15, -15, [0, 0]),
        (-25, -25, [0, 0]),
        (-100, -100, [0, 0]),
    ]
)
def test_modify_classes(
        cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (10, [1, 2]),
        ([1, 2], 10),
        (10, "0"),
        ({"age": 10}, 10),
        (10, None)
    ]
)
def test_get_human_age_invalid_input(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
